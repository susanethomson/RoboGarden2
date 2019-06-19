#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keras.datasets import mnist
# dataset of handwritten numbers 0-9 inside Keras
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#CNN model needs 4 inputs: number of samples, width, height, colour depth)
# colour depth:  greyscale =1, colour = 3 (RGB)
x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

#normalize the input to be scaled to between 0 and 1 - each pixel has value 0-255
x_train = x_train/255
x_test = x_test/255

#sequential is a multi layer perceptron - basic for ANN
from keras.models import Sequential 
model = Sequential()

#convolve input with 3x3 filter
from keras.layers import Conv2D
model.add(Conv2D(28, (3, 3), input_shape=(28, 28, 1), activation='relu'))

#pool to reduce computation time/power while maintaining integrity of the data
from keras.layers import MaxPooling2D 
model.add(MaxPooling2D(pool_size=(2, 2)))

from keras.layers import Flatten 
model.add(Flatten())

#add fully connected feed forward layers 
from keras.layers import Dense 
model.add(Dense(units=128, activation='relu'))

#output layer
model.add(Dense(units=10, activation='softmax'))

#Build CNN model
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

#train model
model.fit(x_train, y_train,epochs=10)

loss, accuracy = model.evaluate(x_test, y_test)

print (loss)
print (accuracy)

