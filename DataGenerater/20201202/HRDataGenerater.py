import numpy as np
import cv2
import random
import time
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random


ImgHeightWidth=608
PaddingMiniValue=5


img=np.zeros((ImgHeightWidth,ImgHeightWidth,3), np.uint8)

def clear_hidden_files(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)



wd = os.getcwd()
work_sapce_dir = os.path.join(wd, "VOCdevkit/")
if not os.path.isdir(work_sapce_dir):
    os.mkdir(work_sapce_dir)

RawData_sapce_dir = os.path.join(wd, "todo/")
if not os.path.isdir(RawData_sapce_dir):
    print("No todo Raw Data!")

work_sapce_dir = os.path.join(work_sapce_dir, "VOC2007/")
if not os.path.isdir(work_sapce_dir):
    os.mkdir(work_sapce_dir)
annotation_dir = os.path.join(work_sapce_dir, "Annotations/")
if not os.path.isdir(annotation_dir):
        os.mkdir(annotation_dir)
clear_hidden_files(annotation_dir)
image_dir = os.path.join(work_sapce_dir, "JPEGImages/")
if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
clear_hidden_files(image_dir)
VOC_file_dir = os.path.join(work_sapce_dir, "ImageSets/")
if not os.path.isdir(VOC_file_dir):
        os.mkdir(VOC_file_dir)
VOC_file_dir = os.path.join(VOC_file_dir, "Main/")
if not os.path.isdir(VOC_file_dir):
        os.mkdir(VOC_file_dir)

train_file = open(os.path.join(wd, "2007_train.txt"), 'w')
test_file = open(os.path.join(wd, "2007_test.txt"), 'w')
train_file.close()
test_file.close()
VOC_train_file = open(os.path.join(work_sapce_dir, "ImageSets/Main/train.txt"), 'w')
VOC_test_file = open(os.path.join(work_sapce_dir, "ImageSets/Main/test.txt"), 'w')
VOC_train_file.close()
VOC_test_file.close()
if not os.path.exists('VOCdevkit/VOC2007/labels'):
    os.makedirs('VOCdevkit/VOC2007/labels')
train_file = open(os.path.join(wd, "2007_train.txt"), 'a')
test_file = open(os.path.join(wd, "2007_test.txt"), 'a')
VOC_train_file = open(os.path.join(work_sapce_dir, "ImageSets/Main/train.txt"), 'a')
VOC_test_file = open(os.path.join(work_sapce_dir, "ImageSets/Main/test.txt"), 'a')
list = os.listdir(RawData_sapce_dir) # list image files
# print(list)
for z in range(0,len(list)):
# for z in range(1,10):
# //生成数据图
    in_path=RawData_sapce_dir + list[z]
    image_path = image_dir + list[z]

    voc_path = list[z]
    (ImgnameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
    (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))


    out_file = open('VOCdevkit/VOC2007/labels/%s.txt' % ImgnameWithoutExtention, 'w')
    img4 = cv2.imread(in_path,1)
    # print(img4.shape[0],img4.shape[1])
    img3 = cv2.applyColorMap(img, cv2.COLORMAP_JET)

    RandomPadding = random.randint(0, 10)+PaddingMiniValue
    # RandomPadding=10
    # if(img4.shape[0] and img4.shape[1]):
    # 写入2007_train.txt 2007_test.txt train.txt test.txt
    probo = random.randint(1, 100)
    print("Probobility: %d" % probo)
    if(probo < 75):
        train_file.write(image_path + '\n')
        VOC_train_file.write(voc_nameWithoutExtention + '\n')
    else:
        test_file.write(image_path + '\n')
        VOC_test_file.write(voc_nameWithoutExtention + '\n')


    try:
        x=random.randint(1,ImgHeightWidth-img4.shape[0]-RandomPadding*2)
        y=random.randint(1,ImgHeightWidth-img4.shape[1]-RandomPadding*2)
        # x=30
        # y=500
        # 写入YOLOMark txt文件
        # x+RandomPadding+img4.shape[0]/2
        b = (float(x), float(x + RandomPadding * 2 + img4.shape[1]), float(y), float(y + RandomPadding * 2 + img4.shape[0]))
        bb = convert((ImgHeightWidth, ImgHeightWidth), b)
        out_file.write(str(int(list[z][0])-1) + " " + " ".join([str(a) for a in bb]) + '\n')
        out_file.close()
        # 生成对应图像
        for i in range(img4.shape[0]):
         for j in range(img4.shape[1]):
          img3[i+y][j+x] = img4[i][j]

        cv2.imwrite(image_path,img3)

    except Exception as e:
        print(in_path,e)

train_file.close()
test_file.close()
VOC_train_file.close()
VOC_test_file.close()