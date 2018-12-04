import os
import numpy as np
from PIL import Image


def getImageValue():
    path = 'vertification Image'

    files = os.listdir(path)
    y_index = 0
    X_dataset = []
    Y_dataset = []
    for file in files:
        image_file = os.listdir(path + '/' + file)
        for image in image_file:
            image_array = Image.open(path + '/' + file + '/' + image).convert('1')
            binary_array = np.array(image_array, dtype='f')
            X_dataset.append(binary_array.reshape(1, binary_array.shape[0] * binary_array.shape[1])[0])
            y = np.zeros([1, 33])
            y[0][y_index] = 1
            Y_dataset.append(y[0])
        y_index += 1

    return X_dataset, Y_dataset


def getCVImageValue(imagePath):
    X_dataset = []
    Y_dataset = []

    image_array = Image.open(imagePath).convert('1')
    binary_array = np.array(image_array, dtype='f')
    X_dataset.append(binary_array.reshape(1, binary_array.shape[0] * binary_array.shape[1])[0])
    y = np.zeros([1, 33])
    y[0][1] = 1
    Y_dataset.append(y[0])

    return X_dataset, Y_dataset
