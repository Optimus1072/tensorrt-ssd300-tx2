from __future__ import print_function

import math
import os
import shutil
import stat
import subprocess
import sys
import cv2

import numpy as np
import caffe
from google.protobuf import text_format

weights_file = "/home/cst/tensorrt-ssd-easy/VGG_VOC0712_SSD_300x300_iter_120000.caffemodel"
deploy_file  = "/home/cst/tensorrt-ssd-easy/deploy1.prototxt"

caffe.set_mode_gpu()
caffe.set_device(0)

image = cv2.imread("000001.jpg", flags=cv2.IMREAD_COLOR)
image = cv2.resize(image, (300,300))
image = np.array(image)
# image = np.transpose(image, (2,0,1))
print (image.shape)
print(image[:,:,0])
print(image[:,:,1])
print(image[:,:,2])

image = image[np.newaxis, :,:,:]

mean = np.array([ 104, 117, 123])
image = image - mean
image = np.transpose(image, (0,3,1,2))
print (image.shape)

net = caffe.Net( deploy_file, weights_file, caffe.TEST)

print (image.shape)

net.blobs['data'].data[...] = image
print (image)
net.forward(end='detection_out')
myData = net.blobs['detection_out'].data
#myData1 = net.blobs['data'].data
#print (myData1)
for i in range(0,myData.shape[2]):
    #print (myData[0,0,i,2])
    if myData[0,0,i,2]>0.1:
       print (myData[0,0,i,:])
#print ("mbox_conf_reshape shape is: ", myData.shape)
#for i in range(200):
	#print (myData[:,:,i,:])
# print (myData)
# print (myData[0,:42])
