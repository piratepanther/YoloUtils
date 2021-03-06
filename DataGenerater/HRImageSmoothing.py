import cv2
import numpy as np
import time

#Variables
ImageName="2020-12-02-18-30-51"
ResizeWight=15000
ResizeHeightScale=5.5
#ProcessingRoad
img = cv2.imread("20201202/HRimage/"+ImageName+".jpg", cv2.IMREAD_UNCHANGED)

Height, Wight = img.shape[0:2]

ResizeHeight=Height*ResizeHeightScale
# Height= img.shape[0]
img_Resize = cv2.resize(img, (int(ResizeWight), int(ResizeHeight)),interpolation=cv2.INTER_LINEAR)


cv2.imshow("Image", img)
cv2.imshow("Img_Resize", img_Resize)

# #GaussianBlur
# img_gauss = cv2.GaussianBlur(img,(5,5),1)
# cv2.imshow("img_gauss",img_gauss)

# #Blur
# img_blur = cv2.blur(img,(3,3))
# cv2.imshow("img_blur", img_blur)

# #medianblur
# img_medianblur = cv2.medianBlur(img,3)
# cv2.imshow("img_medianblur", img_medianblur)

# #bilateral
# img_bilateral = cv2.bilateralFilter(img,0,0.2,40)
# cv2.imshow("img_bilateral", img_bilateral)

# #joint
# img_gauss = cv2.GaussianBlur(img,(5,5),1,0)
# joint = cv2.ximgproc.jointBilateralFilter(img_gauss,img,33,2,0)
# cv2.imshow("img_joint", img_joint)






cv2.waitKey(0)

cv2.destroyAllWindows()