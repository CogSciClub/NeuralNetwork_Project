import sys

env_check_msg = 'ENV CHECK: '

def print_msg(msg):
	print(env_check_msg + str(msg))

def print_err(msg, error=''):
	for i in range(7):
		print_msg('Uh Oh...')
	print_msg('Something isn\'t right...')
	print_msg(msg)
	if len(str(error)) > 0:
		print_msg(error)
	for i in range(7):
		print_msg('Uh Oh...')
	input('Save the above message somewhere and hit enter to continue...')

print_msg('Checking Python version . . .')
required_version = '3.6.5'
required_maxsize = 2**32
actual_version = str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])
if actual_version != required_version:
	print_err('Python version ' + required_version + ' is required, but the version being used is ' + actual_version + '.')
elif sys.maxsize < required_maxsize:
	print_err('Python 64-bit is required, but 32-bit is being used.')
else:
	print_msg('Python version looks good!')

print_msg('Checking dependencies . . .')
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
	print_msg('Dependencies look good!')
except Exception as e:
	print_err('Oops, a dependency doesn\'t seem to be working.', e)
