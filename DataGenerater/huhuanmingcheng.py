import numpy as np
import cv2
import random
import time
#img=np.zeros((608,608,3), np.uint8)
#ronghetu1
totalnum=13000

for z in range(20000):

    randnum = random.randint(0, totalnum-1)
    randnum1 = random.randint(0, totalnum-1)
    in_path='J:/data/yolo/todo/retodo/strike/'+str("%05d" % randnum)+'.jpg'
    in_path1 = 'J:/data/yolo/todo/todo/wind/' + str("%05d" % randnum1) + '.jpg'
    out_path2='J:/data/yolo/todo/todo/wind/50000.jpg'
    out_path= in_path1
    out_path1 = in_path

    img = cv2.imread(in_path,1)
    img1 = cv2.imread(in_path1, 1)

    # if(img4.shape[0] and img4.shape[1]):
    try:
        cv2.imwrite(out_path2, img)
        img2 = cv2.imread(out_path2, 1)
        cv2.imwrite(out_path1, img1)
        cv2.imwrite(out_path, img2)

    except Exception as e:
        print(in_path1,in_path,e)
print('done!!!!!!!!')