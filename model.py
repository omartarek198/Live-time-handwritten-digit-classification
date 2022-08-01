import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import os
from PIL import Image
import  PIL


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        print ("done")
        im = Image.open(folder + "//" +filename)
        im = PIL.ImageOps.invert(im)
        im = im.resize((28, 28))


        im = im.convert('L')
        im = np.asarray(im)
        im = np.expand_dims(im, -1)

        im = im.astype("float32") / 255
        if im is not None:
            images.append(im)
    return images
# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)



# Load the data and split it between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

#Loading Operator Data Manually

print (y_train.shape)

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)



print (y_train.shape)
print("x_train shape:", x_train.shape)
print(x_train[0].shape, "train samples")
print(x_test.shape[0], "test samples")


# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)

print ("after", y_train.shape)
print(y_train[-1])
y_test = keras.utils.to_categorical(y_test, num_classes)

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu",padding="same"),
        layers.MaxPooling2D(pool_size=(2, 2),padding = 'same'),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu",padding="same"),
        layers.MaxPooling2D(pool_size=(2, 2),padding='same'),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()

batch_size = 128
epochs = 15


model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)


score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

model.save("model.h5")