from HRfeatureExtraction import featExtraUtils
import cv2
import numpy as np
from HRfeatureExtraction import featExtraDTO

# in_path = '123.png'
#
# #cv2.IMREAD_COLOR忽略alpha通道cv2.IMREAD_GRAYSCALE读入灰度图片cv2.IMREAD_UNCHANGED
#
#
#
#
# img = cv2.imread(in_path)
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
#
# cv2.imshow("img", img)
# cv2.waitKey(0)

print(type(featExtraDTO.alertLevel.LEVEL1.value))
print(type(featExtraDTO.alertLevelCol.BLUE.value))

# bgr_img = cv2.imread(in_path)
# gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
# # b=123
# # a=featExtraUtils.calcuSignalEnergyfromMat(b)
# # x= np.ones(gray_img.shape, dtype = int)
#
# # x=len(gray_img[gray_img > np.mean(gray_img)].tolist())
# # v=[1,2,3,5,6,7]
# x=gray_img[gray_img > np.mean(gray_img)].tolist()
# # print(len(v))
# b=np.arange(24).reshape(4,6)
# print(b)
# print('---------')
# a=b[0:3,0:2]
# print(a)
# print(featExtraUtils.calcuSignalProportionfromMat(gray_img))
# print(type(gray_img[gray_img > np.mean(gray_img)]))
# print(x)
# print(gray_img.shape)

