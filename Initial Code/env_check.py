import sys

env_check_msg = 'ENV CHECK: '

print(env_check_msg + 'Checking Python version . . .')
required_version = '3.6.5'
required_maxsize = 2**32
actual_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
if actual_version != required_version:
	print(env_check_msg + 'Python version ' + required_version + ' is required, but the version being used is ' + actual_version + '.')
elif sys.maxsize < required_maxsize:
	print(env_check_msg + 'Python 64-bit is required, but 32-bit is being used.')
else:
	print(env_check_msg + 'Python version looks good!')

print(env_check_msg + 'Checking dependencies . . .')
try:
	import imutils
	import cv2
	import numpy as np
	import pandas as pd
	from keras.callbacks import CSVLogger, ModelCheckpoint, EarlyStopping
	from keras.callbacks import ReduceLROnPlateau
	from keras import layers
	from keras.layers import Activation, Convolution2D, Dropout, Conv2D
	from keras.layers import AveragePooling2D, BatchNormalization
	from keras.layers import GlobalAveragePooling2D
	from keras.layers import Flatten
	from keras.layers import Input
	from keras.layers import MaxPooling2D
	from keras.layers import SeparableConv2D
	from keras.models import Sequential
	from keras.models import Model
	from keras.models import load_model
	from keras.preprocessing.image import ImageDataGenerator
	from keras.preprocessing.image import img_to_array
	from keras.regularizers import l2
	from sklearn.model_selection import train_test_split
	print(env_check_msg + 'Dependencies look good!')
except Exception as e:
	print(env_check_msg + 'Oops, a dependency doesn\'t seem to be working.')
	print(env_check_msg + 'ERR: ' + str(e))
