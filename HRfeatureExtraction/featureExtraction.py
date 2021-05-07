import cv2



in_path = '123.png'

#cv2.IMREAD_COLOR忽略alpha通道cv2.IMREAD_GRAYSCALE读入灰度图片cv2.IMREAD_UNCHANGED
img = cv2.imread(in_path,cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()