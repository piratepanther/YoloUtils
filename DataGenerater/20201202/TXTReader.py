import numpy as np
import cv2
import random
import time

# annopath = os.path.join(
#     'labels',
#     '{:s}.txt')
#
# print(annopath)

devkit_path='VOCdevkit'
year='2007'
txtName='1-'
annopath = os.path.join(
    devkit_path,
    'VOC' + year,
    'labels',
    txtName+'.txt')

with open(annopath,"w") as f:
     f.write(DataContent3)




# randnum=00000
# randnum2=123123123
# DataContent=""
# # DataContent2="1 0.2064144736842105 0.4786184210526315 0.28125 0.03289473684210526\n0 0.8495065789473684 0.41447368421052627 0.02796052631578947 0.07236842105263158\n"
#
# in_path='J:/data/yolo/20201221 data/VOCdevkit/VOC2007/labels/'+str("%05d" % randnum)+'.txt'
# out_path='J:/data/yolo/20201221 data/VOCdevkit/VOC2007/labels/'+str("%05d" % randnum2)+'.txt'
#
# with open(in_path, "r") as f:  # 打开文件
#     # data = f.read()  # 读取文件
#     # data = f.readlines()
#     # DataContent=data
#     data = f.readline()
#     print(data)
#
# # print(DataContent)
# #
# # with open(out_path,"w") as f:
# #     for i in DataContent:
# #         f.write(i)
#
#
# DataContent3=""
# DataContent3+="123"
# DataContent3+=" "
# DataContent3+="312"
# DataContent3+="\n"
# DataContent3+="123"
# DataContent3+=" "
# DataContent3+="312"
# print(DataContent3)
# with open(out_path,"w") as f:
#      f.write(DataContent3)