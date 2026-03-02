# Handwritten Digit Recognizer

A neural network that recognizes handwritten digits 0-9 using the MNIST dataset. Built with TensorFlow and Keras, achieving 97% accuracy on unseen test data.

## How It Works

The model is trained on 60,000 handwritten digit images from the MNIST dataset. Each image is 28x28 pixels, flattened to 784 numbers and normalized between 0 and 1. A 3 layer neural network then learns the patterns between pixel values and the correct digit.

## Model Architecture

- Input layer — 784 neurons (one per pixel)
- Hidden layer 1 — 128 neurons with ReLU activation
- Hidden layer 2 — 64 neurons with ReLU activation
- Output layer — 10 neurons with Softmax activation (one per digit)

## Results

- Training accuracy: 99.4%
- Test accuracy: 97%

## What I Learned

- Neural networks and how they differ from traditional ML models
- Image data representation as pixel arrays
- Data normalization and flattening
- Multiclass classification with 10 output classes
- Epochs and batch training
- TensorFlow and Keras

## Tech Stack

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib

## Dataset

MNIST handwritten digits dataset — 60,000 training images and 10,000 test images, built into TensorFlow.
