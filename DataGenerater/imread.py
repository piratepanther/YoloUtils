import cv2
import numpy as np
import time


begin_row=0
step_row=50
# begin_column=0
# step_column=100
vibration_point=2338



step_column=25

img = cv2.imread("J:/huarunranqi/watu/watu/2019-05-06-15-22-21.jpg", 0)

# img2= np.array(img)
# img2=img[begin_row:begin_row+step_row, begin_column:begin_column+step_column]
# img2=img[:, :]
# img2=cv2.resize(img,(3072,300),interpolation=cv2.INTER_CUBIC)
for i in range(-10,15,5):
    # vibration_point = vibration_point+i
    img2=img[begin_row:begin_row+step_row, vibration_point+i-step_column:vibration_point+i+step_column]

# print(img.shape,img.size,img.dtype,378*421,type(img),img)
# print(img2.shape,img2.size,img2.dtype,378*421,type(img2),img2)
# img2=img.reshape(400,300)
    path="J:/huarunranqi/biaozhun/watu/test/"+str(i // 5 +2+5*15)+".jpg"
    cv2.imwrite(path,img2)
    # cv2.imshow("img2", cv2.imread("J:/data/20190122kaifeng/2st/zhendong/1.png"))
    # cv2.imwrite("canny.jpg", cv2.Canny(img, 200, 300))
    # cv2.imshow("canny", cv2.imread("canny.jpg"))
    # cv2.waitKey()
    # time.sleep(5)
    cv2.destroyAllWindows()
# cv2.imshow('new',img2)
# cv2.imshow('old',img)
# cv2.waitKey(0)
# cv2.destoryAllWindows()


