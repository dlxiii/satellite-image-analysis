# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:32:39 2019

@author: Yulong
"""

import json, sys, random
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.layers import Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras.optimizers import SGD
import keras.callbacks
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
 

path = '../data/samples'
file = 'site6_zoom_20.tif'

##read image
#img = Image.open(path + '/' + file)
# 
##view the image 
#img.show()

#read image
img_arr = plt.imread(path + '/' + file)
 
#view image
plt.imshow(img_arr)
plt.show()