from HRfeatureExtraction import featExtraUtils
import cv2
import numpy as np


in_path = '123.png'

#cv2.IMREAD_COLOR忽略alpha通道cv2.IMREAD_GRAYSCALE读入灰度图片cv2.IMREAD_UNCHANGED

bgr_img = cv2.imread(in_path)
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
# b=123
# a=featExtraUtils.calcuSignalEnergyfromMat(b)
# x= np.ones(gray_img.shape, dtype = int)

# x=len(gray_img[gray_img > np.mean(gray_img)].tolist())
# v=[1,2,3,5,6,7]
x=gray_img[gray_img > np.mean(gray_img)].tolist()
# print(len(v))
b=np.arange(24).reshape(4,6)
print(b)
print('---------')
a=b[0:3,0:2]
print(a)
print(featExtraUtils.calcuSignalProportionfromMat(gray_img))
print(type(gray_img[gray_img > np.mean(gray_img)]))
print(x)
print(gray_img.shape)

