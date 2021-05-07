import cv2
from HRfeatureExtraction import featExtraUtils
import numpy as np
#@paramter
in_path = '123.png'
signalStrengthThreshold=100 #0-255
hightThre=5
widththre=3
areathre=5

#cv2.IMREAD_COLOR忽略alpha通道cv2.IMREAD_GRAYSCALE读入灰度图片cv2.IMREAD_UNCHANGED
#mian
bgr_img = cv2.imread(in_path)
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
# img = cv2.imread(in_path,cv2.IMREAD_GRAYSCALE)
# print (type(bgr_img))
# print (type(gray_img))
#grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

signalEnergy=featExtraUtils.calcuSignalEnergyfromMat(gray_img)
signalMax=featExtraUtils.calcuSignalMaxfromMat(gray_img)
signalMean=featExtraUtils.calcuSignalMeanfromMat(gray_img)
signalVar=featExtraUtils.calcuSignalVarfromMat(gray_img)
signalProportion=featExtraUtils.calcuSignalProportionfromMat(gray_img)
vibrationDegree=featExtraUtils.calcuVibrationDegreefromMat(gray_img,signalStrengthThreshold,hightThre,widththre,areathre)

print('--------')
print(signalEnergy,signalMax,signalMean,signalVar,str(signalProportion)+'%',str(vibrationDegree)+'%')

cv2.imshow('image',bgr_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ret, binary = cv2.threshold(gray_img, signalStrengthThreshold, 255, cv2.THRESH_BINARY)
#
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE,  cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(bgr_img, contours[0],-1, (0, 0, 255), -1)#0-max分别对应右下角至左上角按行排序
# cv2.drawContours(bgr_img, contours[len(contours)-1],-1, (0, 255, 0), -1)
#featExtraUtils.calcuSignalEnergyfromMat()

# bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]
#
# for bbox in bounding_boxes:
#     [x, y, w, h] = bbox
#     cv2.rectangle(bgr_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# [x1, y1, w1, h1]=cv2.boundingRect(contours[0])
#
# [x2, y2, w2, h2]=cv2.boundingRect(contours[len(contours)-1])


# print([x1, y1, w1, h1])
# eligibleContours=[]
# for contour in contours:
#     [x, y, w, h]=cv2.boundingRect(contour)
#     area = cv2.contourArea(contour)
#     if w>widththre and h>hightThre and area>areathre:
#         eligibleContours.append(contour)
#         cv2.rectangle(bgr_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     else:
#         continue
# for(t=0;t<len(contours);t++)
#    {
#        cv::Rect rect_waring=cv::boundingRect(contours[t]);
#
#         if(rect_waring.height<hightThre)
#         {
#             continue;
#         }
#         if(rect_waring.width<widththre)
#         {
#             continue;
#         }
#         double area=cv::contourArea(contours[t]);
#         if(area<areathre)
#         {
#             continue;
#         }
#     }
# print (type(contours))
# print (type(contours[300]))
# print (len(contours[300]))
# print (contours[300])
# print (len(contours))
