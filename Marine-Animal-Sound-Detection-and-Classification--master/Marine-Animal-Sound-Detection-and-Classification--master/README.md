# Marine Audio Classification using CNN and ResNet50

This project utilizes Convolutional Neural Networks (CNN) and ResNet50 architecture to perform audio classification. We have employed mel frequency features and converted audio data into images for training and testing.

## Overview

Audio classification is the task of assigning a label to an audio sample from a set of predefined labels. In this project, we aim to classify audio data into different categories using machine learning techniques. To achieve this, we have employed a combination of CNN and ResNet50 architectures, leveraging mel frequency features and image conversion techniques.

## Features

- **CNN and ResNet50 Architectures:** We have implemented both CNN and ResNet50 architectures for audio classification, allowing for flexibility and comparison between the two models.
- **Mel Frequency Features:** Mel frequency features are extracted from audio data using librosa library, capturing essential characteristics of the audio signal.
- **Audio to Image Conversion:** Audio data is converted into images using the extracted mel frequency features. These images are then used as input for training and testing the models.
- **High Accuracy:** Our trained models achieve impressive accuracy, with a training accuracy of 97% and a test accuracy of 92%.

## Requirements

- Python 3.x
- NumPy
- TensorFlow
- Keras
- Librosa

Install the required packages using pip:

