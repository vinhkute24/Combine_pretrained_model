# Project Title
BRAIN TUMOR CLASSIFICATION USING COMBINATION PRETRAINED CONVOLUTIONAL NEURAL NETWORK (CNN) MODELS

Here, I try to improve the process of transfer learning (TL) by combining two pre-trained CNN models which are InceptionV3, MobilenetV3 to detect of brain tumor.

## Installation Guide for Running the Code in Jupyter Notebook

This guide provides step-by-step instructions on how to install the required dependencies for running the code in Jupyter Notebook. 

## Prerequisites
- Python 3.x
- Jupyter Notebook

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
6. Download the pre-trained models:  
6.1. InceptionV3:
```python
from keras.applications import InceptionV3
model = InceptionV3(weights='imagenet')
```
6.2. MobileNetV3:
```python
from keras.applications import MobileNetV3
model = MobileNetV2(weights='imagenet')
```
7. Run the code in Jupyter Notebook:  
Launch Jupyter Notebook:
```bash
jupyter notebook
```
8. Open these code file (inception.ipynb, mobileNetV3.ipynb, thesis_final.ipynb) and execute the cells. 
