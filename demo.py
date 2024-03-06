import tkinter as tk
from tkinter import filedialog
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import cv2
from PIL import ImageTk, Image

# Load the pre-trained Keras model
model = load_model('C:/Users/Admin/Downloads/thesis/nhap/model_demo.h5')

def predict(model, img_path):
    img = image.load_img(img_path, target_size=(299, 299))

    # Preprocess the image
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0 
    
    predictions = model.predict(img)
    
    class_labels = ['notumor', 'glioma', 'meningioma', 'pituitary']
    predicted_class_index = np.argmax(predictions[0])

    # Map the predicted class index to the corresponding label
    predicted_class_label = class_labels[predicted_class_index]
    return predicted_class_label

# Define the function for the "Upload Image" button
def upload_images():
    file_paths = filedialog.askopenfilenames()
    results = []
    for file_path in file_paths:
        result = predict(model, file_path)
        results.append(result)
        display_image(file_path, result)

# Define the function for the "Capture Image" button
def capture_image():
    # Create a new window for the camera interface
    capture_window = tk.Toplevel(window)

    # Create a label to display the camera feed
    camera_label = tk.Label(capture_window)
    camera_label.grid(row=0, column=0)

    # Initialize the camera capture
    cap = cv2.VideoCapture(0)

    def update_camera():
        ret, frame = cap.read()
        if ret:
            # Convert the frame to PIL format
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img)

            # Resize the image to fit the label
            img_pil = img_pil.resize((300, 300), Image.ANTIALIAS)

            # Create a PhotoImage and update the label
            img_tk = ImageTk.PhotoImage(img_pil)
            camera_label.img = img_tk  # Keep a reference to avoid garbage collection
            camera_label.config(image=img_tk)

        # Schedule the next update
        capture_window.after(10, update_camera)

    # Start the camera feed
    update_camera()
    
    def capture_frame():
        # Read the current frame from the camera
        ret, frame = cap.read()
        if ret:
            # Save the captured frame as an image file
            cv2.imwrite('capture.jpg', frame)
            result =  predict(model, 'capture.jpg')

            display_image('capture.jpg', result)

            # Close the capture window and destroy associated widgets
            capture_window.destroy()

    # Create the "Capture" button
    capture_button = tk.Button(capture_window, text="Capture", command=capture_frame)
    capture_button.grid(row=1, column=0, pady=10)

# Define the function to display the image

def display_image(image_path, result):
    # Load and resize the image
    img = Image.open(image_path)
    img = img.resize((100, 100))

    # Convert the image to PhotoImage format
    img_tk = ImageTk.PhotoImage(img)

    # Find the first available image label and result label
    for i in range(len(image_labels)):
        if image_labels[i]["state"] == "empty":
            # Update the image label
            image_label = image_labels[i]["label"]
            image_label.config(image=img_tk)
            image_label.image = img_tk

            # Update the result label
            result_label = result_labels[i]["label"]
            result_label.config(text="Predicted: " + result)

            # Update the state of the image label and result label
            image_labels[i]["state"] = "occupied"
            result_labels[i]["state"] = "occupied"

            break

# Define the function to reset the image labels and result labels
def reset():
    # Reset the state of all image labels and result labels
    for label in image_labels:
        label["state"] = "empty"
        label["label"].config(image="")
    for label in result_labels:
        label["state"] = "empty"
        label["label"].config(text="")


# Create the main window
window = tk.Tk()
window.geometry("1280x720")  # Set the window size to 1280x720 pixels
window.title("Image Classification")

# Create a frame to hold the image grid
image_frame = tk.Frame(window)
image_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Create the "Upload Image" button
upload_button = tk.Button(window, text="Upload Image", command=upload_images)
upload_button.grid(row= 0, column= 0, padx=10, pady=10)

# Create the "Capture Image" button
capture_button = tk.Button(window, text="Capture Image", command=capture_image)
capture_button.grid(row= 0, column= 1, padx=10, pady=10)

# Create the "Reset" button
reset_button = tk.Button(window, text="Reset", command=reset)
reset_button.grid(row=0, column= 2, padx=10, pady=10)

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.grid(row=0, column=0, columnspan=3)

# Add buttons to the button frame
upload_button.grid(row=0, column=0, padx=10, pady=10)
capture_button.grid(row=0, column=1, padx=10, pady=10)
reset_button.grid(row=0, column=2, padx=10, pady=10)

# Lists to store image labels and result labels
image_labels = []
result_labels = []

# Create the image labels grid
for i in range(5):
    for j in range(4):
        # Create a frame for each image and result
        frame = tk.Frame(image_frame, width=100, height=100)
        frame.grid(row=i, column=j, padx=5, pady=5)

        # Create the image label
        img_label = tk.Label(frame)
        img_label.pack(side=tk.LEFT)

        # Create the result label
        result_label = tk.Label(frame, text="")
        result_label.pack(side=tk.RIGHT)

        # Store the image label and result label in a dictionary
        image_labels.append({"label": img_label, "state": "empty"})
        result_labels.append({"label": result_label, "state": "empty"})

# Run the application
window.mainloop()