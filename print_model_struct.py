#! /usr/bin/python

from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import load_model

net = load_model('model/model-resnet50-final.h5')
net._layers.pop(-1)
print(net.summary())
