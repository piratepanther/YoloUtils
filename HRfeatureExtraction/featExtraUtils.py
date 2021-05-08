import cv2
import numpy as np
from HRfeatureExtraction import featExtraDTO

#计算灰度图像区域内能量
def calcuSignalEnergyfromMat( gray_img ):
   assert type(gray_img)==np.ndarray
   return np.sum(np.power(gray_img, 2))

def calcuSignalMaxfromMat( gray_img ):
   assert type(gray_img)==np.ndarray
   return np.amax(gray_img)

def calcuSignalMeanfromMat(gray_img):
   assert type(gray_img) == np.ndarray

   return np.mean(gray_img)

def calcuSignalVarfromMat(gray_img):
   assert type(gray_img) == np.ndarray
   return np.var(gray_img)

def calcuSignalProportionfromMat(gray_img):
   assert type(gray_img) == np.ndarray
   # gray_img.shape
   totleLen=len(gray_img.tolist())
   upMeanlen=len(gray_img[gray_img > np.mean(gray_img)].tolist())
   return upMeanlen/totleLen

def calcuVibrationDegreefromMat(gray_img,signalStrengthThreshold=100,hightThre=5,widththre=3,areathre=5):
   assert type(gray_img) == np.ndarray
   assert type(signalStrengthThreshold) == int
   assert type(hightThre) == int
   assert type(widththre) == int
   assert type(areathre) == int
   ret, binary = cv2.threshold(gray_img, signalStrengthThreshold, 255, cv2.THRESH_BINARY)

   contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
   eligibleContours = []
   for contour in contours:
      [x, y, w, h] = cv2.boundingRect(contour)
      area = cv2.contourArea(contour)
      if w > widththre and h > hightThre and area > areathre:
         eligibleContours.append(contour)
      else:
         continue
   # if eligibleContours:
   [x1, y1, w1, h1]=cv2.boundingRect(eligibleContours[0])

   [x2, y2, w2, h2]=cv2.boundingRect(eligibleContours[len(eligibleContours)-1])

   gray_img_Before = gray_img[y1: y1 + h1, x1: x1 + w1]
   gray_img_After = gray_img[y2: y2 + h2, x2: x2 + w2]

   return (calcuSignalMeanfromMat(gray_img_Before)-calcuSignalMeanfromMat(gray_img_After))/255


def calcuAlertLevelNum(signalEnergy,signalMax ,signalMean, signalVar, signalProportion, vibrationDegree):
   alertLevelNum = signalEnergy*featExtraDTO.alertLevelParameter.signalEnergyPara.value + \
                   signalMax*featExtraDTO.alertLevelParameter.signalMaxPara.value+ \
                   signalMean*featExtraDTO.alertLevelParameter.signalMeanPara.value+ \
                   signalVar*featExtraDTO.alertLevelParameter.signalVarPara.value+ \
                   signalProportion*featExtraDTO.alertLevelParameter.signalProportionPara.value+ \
                   vibrationDegree*featExtraDTO.alertLevelParameter.vibrationDegreePara.value

   return alertLevelNum