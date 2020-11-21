import numpy as np
import cv2
import random
import matplotlib.pyplot as plt

#########################################################
totalnum=1000
totalnum1=15
for z in range(10):

    randnum = random.randint(0, totalnum)
    randnum1 = random.randint(0, totalnum1)
    in_path1 = 'J:/data/yolo/todo/retodo/strike/' + str("%05d" % randnum) + '.jpg'

    in_path = 'J:/data/yolo/todo/todo/wind/' + str("%05d" % randnum1) + '.jpg'
    img1 = cv2.imread(in_path, 1)  # zhutu
    print(img1)
    print(in_path1)
    print('####################################')
    # out_path='J:/data/yolo/todo/retodo/ronghe/'+str("%05d" % z)+'.jpg'
    #
    # img = cv2.imread(in_path,1) #zhutu
    # img1 = cv2.imread(in_path1, 1)  #daironghetu
    #
    # # if(img4.shape[0] and img4.shape[1]):
    # try:
    #     x=random.randint(1,608-img1.shape[0])
    #     y=random.randint(1,608-img1.shape[1])
    #     for i in range(img1.shape[0]):
    #      for j in range(img1.shape[1]):
    #         if ((img[i+x][j+y] == [128,0,0]).all()):
    #             img[i+x][j+y] = img1[i][j]
    #         else:
    #             pass
    #
    #     cv2.imwrite(out_path,img)
    #
    # except:
    #     print(in_path)
#########################################################
# img=np.zeros((608,608,3), np.uint8)
# img4 = cv2.imread('J:/data/yolo/2019-07-25-17-00-43/Img(2)/Img(1)/Img/todo/strike/00002.jpg',1)
# # cv2.line(img,(0,0),(511,511),(255,0,0),5)
# img3 = cv2.applyColorMap(img, cv2.COLORMAP_JET)
# print(img3)
##########################################################
# img3=np.zeros((5,5,3), np.uint8)#new pic
# # img3=np.array([[[0,0,0],[0,0,0]],[[0,2,0],[3,0,0]]])#new pic
# img4=np.array([[[0,4,0],[0,1,0]],[[0,2,0],[3,0,0]]])#shijian
#
# a=np.array([128,0,0])
# b=np.array([128,0,0])
# for z in range(3):
#  img = np.zeros((608, 608, 3), np.uint8)
#  img4 = cv2.imread('J:/data/yolo/2019-07-25-17-00-43/Img(2)/Img(1)/Img/todo/strike/00002.jpg', 1)
#  # cv2.line(img,(0,0),(511,511),(255,0,0),5)
#  img3 = cv2.applyColorMap(img, cv2.COLORMAP_JET)
#
#
#  x=random.randint(1,608-img4.shape[0])
#  y=random.randint(1,608-img4.shape[1])
#  for i in range(img4.shape[0]):
#   for j in range(img4.shape[1]):
#    img3[i+x][j+y] = img4[i][j]
#
#  # print(img3)
#  # print(img3.shape)
#  # cv2.imshow('image',img3)
#  # cv2.waitKey(0)
#  out_path='J:/data/yolo/2019-07-25-17-00-43/Img(2)/Img(1)/Img/retodo/strike/'+str("%05d" % z)+'.jpg'
#  cv2.imwrite(out_path,img3)
# cv2.destroyAllWindows()
###########################################################
# img3=np.zeros((2,2,3), np.uint8)#new pic
# img4=np.array([[[0,0,0],[0,1,0]],[[0,2,0],[3,0,0]]])#shijian
#
# for i in range(img4.shape[0]):
#
# #  for j in img4.shape[1]:
# #   if((img3[i][j] == img4[i][j]).all()):
# #    pass
# #   else:
# #    img3[i][j] = img4[i][j]
# #
#  print(img4[i])

# for i in range(img4.shape[0]):
#  for j in range(img4.shape[1]):
#   if((img3[i][j] == img4[i][j]).all()):
#    pass
#   else:
#    img3[i][j] = img4[i][j]
#
# print(img3)
# print(img3.shape)
# a==b?
# for i in a==b:
#  if(i):
#    print('true')
#  else:
#    print('flase')


# print(img4==img3)
# print(im_color.shape)
# print(img.shape)
# print(im_color[1][2])
# print(img4.shape)
# cv2.imshow('image',im_color)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# cap = cv2.VideoCapture(0)
#
# while(True):
#  # Capture frame-by-frame
#   ret, frame = cap.read()
#
#
#  # Our operations on the frame come here (cv2.COLOR_BGR2RGB cv2.COLOR_RGB2HSV)
#  #  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#  # Display the resulting frame
#   cv2.imshow('frame',gray)
#   if cv2.waitKey(1) & 0xFF == ord('q'):
#    break
#
#  # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()





# img = cv2.imread('J:/data/yolo/2019-07-25-17-00-43/Img(2)/Img(1)/Img/todo/strike/00002.jpg',1)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# data=np.zeros(shape=(50,90000))
# print(data,type(data),data.shape)
# path="J:/data/20190122kaifeng/2st/biaozhun/zhendong/1.png"
# img = cv2.imread(path, 0)
# data[1,:]=img.reshape(1,img.size)
# # print(type(img.ravel().tolist()))
# # print(img.shape,img.reshape(1,img.size).shape,type(img.ravel()))
# # data[0,:]=img.ravel()
# print(data)

# for i in range(-15,20,5):
#     # print(i)
#     print(str(i // 5 +3+7*3))
# for i in range(0,2):
#
#     img = [1,2,3,4,5]
#     data[i,:]=img
#
#
# img = np.arange(64).reshape(8,8)
# print(img,type(img))
# for i in range(2,4):
#     list=[0,1,2,3,4,5,6,7]
#     array=np.array((0,1,2,3,4,5,6,7))
#     img[i,:]=array
#     print(img[i,:],type(img[i,:]))
# print(img)

# print(img,type(img),type(np.arange(64)),img.reshape(1,img.size))

# j=100
# z=4
# img = np.arange(64).reshape(8,8)
# # print(img,type(img))
# for i in range(0,3):
#     print(i)
#     # img2=img[:,z+i-1:z+i+1]
#     # print(z+i-1,z+i+1,img2)
#     # print(i,z+i,z+i - 1, z +i+ 1)
#     # path = "J:/data/20190122kaifeng/2st/zhendong/" + str(i+8) + ".png"
#     # # print(i+j)
#     # print(path)
#
# # print(j)
# train=np.array(())
# print(type(train),train)

# path="J:/huarunranqi/2800mche/2800/2019-04-30-18-25-04.jpg"
# img = cv2.imread(path, 0)
# print(img.shape[0])