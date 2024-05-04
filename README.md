# Brain Tumor Classification Using Combination Pretrained Convolutional Neural Network (CNN) Models

In this research, I try to improve the process of transfer learning (TL) by combining two pre-trained CNN models which are InceptionV3, MobilenetV3 to classify three types of brain tumor.

## Installation Guide for Running the Code in Jupyter Notebook

This guide provides step-by-step instructions on how to install the required dependencies for running the code in Jupyter Notebook and running the demo application. 

## Prerequisites
- Ensure that you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).
- Jupyter Notebook by using pip
  ```bash
  pip install jupyter
  ```

## Installation Steps

1. Install NumPy, Pandas, and Matplotlib:

```python
pip install numpy pandas matplotlib
```
2. Install TensorFlow and Keras:
```python
pip install tensorflow keras
```
3. Install OpenCV:
```python
pip install opencv-python
```
4. Install Scikit-learn:
```python
pip install scikit-learn
```
5. Install Pillow:
```python
pip install pillow
```
6. Run the code in Jupyter Notebook:  
Launch Jupyter Notebook:
```bash
jupyter notebook
```
7. Open these code file (inception.ipynb, mobileNetV3.ipynb, thesis_final.ipynb) and execute the cells. 

## Guide for Running the demo application (demo.py)
1. Based on previous installed libraries, we can run the demo application to classify brain tumor from the combine CNNs models (MobileNetV3, InceptionV3)
   ```bash
   python demo.py
   ```
