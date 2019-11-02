#! /usr/bin/python

from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import load_model, Model

net = load_model('model/model-resnet50-final.h5')
#net._layers.pop(-1)
#print(net.summary())

# create feature extractor by removing the last layer
input = net.input
output = net.layers[-3].output
model = Model(input, output)
model.summary()
