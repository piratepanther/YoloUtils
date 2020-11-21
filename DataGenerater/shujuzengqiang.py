import numpy as np
import cv2
import random
import time

totalnum=201
moweibiaozhu=201
for z in range(totalnum):

    in_path='J:/data/yolo/todo/todo/strike/'+str("%05d" % z)+'.jpg'
    out_path='J:/data/yolo/todo/todo/strike/'+str("%05d" % (z+1+moweibiaozhu))+'.jpg'

    img = cv2.imread(in_path,1)

    try:
        img2 = cv2.flip(img, 1)
        #img2 = cv2.flip(img, 1)
        #img3 = cv2.flip(img, 0)
        #img4 = cv2.flip(img, -1)

        cv2.imwrite(out_path, img2)

    except Exception as e:
        print(in_path,e)