import  pandas as pd
import pygame
import numpy
import tensorflow
from tensorflow import keras


model = keras.models.load_model('model.h5')

from PIL import Image

def recognize(im):
    # open method used to open different extension image file

    # im = Image.open(r"8small.png")
    # im = Image.open(r"1.png")
    im = im.resize((28, 28))

    im = im.convert('L')
    im = numpy.asarray(im)
    im = numpy.expand_dims(im, 0)
    im = im.astype("float32") / 255
    print(im.shape)

    # print(im)

    y_pred = model.predict(im)

    max = -1
    index = 0

    for i in range(len(y_pred[0])):
        if (y_pred[0][i] > max):
            max = y_pred[0][i]
            index = i

    print(index)
    
    return index,max

recognize( Image.open(r"1.png"))