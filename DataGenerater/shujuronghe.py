import numpy as np
import cv2
import random
import time
#img=np.zeros((608,608,3), np.uint8)
#ronghetu1
totalnum=3000
#ronghetu2
totalnum1=1826
for z in range(4000):

    randnum = random.randint(0, totalnum-1)
    randnum1 = random.randint(0, totalnum1-1)
    in_path='J:/data/yolo/todo/retodo/strike/'+str("%05d" % randnum)+'.jpg'
    in_path1 = 'J:/data/yolo/todo/todo/wind/' + str("%05d" % randnum1) + '.jpg'
    out_path='J:/data/yolo/todo/retodo/ronghe/'+str("%05d" % z)+'.jpg'

    img = cv2.imread(in_path,1) #zhutu
    img1 = cv2.imread(in_path1, 1)  #daironghetu

    # if(img4.shape[0] and img4.shape[1]):
    try:
        x=random.randint(1,608-img1.shape[0])
        y=random.randint(1,608-img1.shape[1])
        for i in range(img1.shape[0]):
         for j in range(img1.shape[1]):
            if ((img[i+x][j+y] == [128,0,1]).all()):
                img[i+x][j+y] = img1[i][j]
            else:
                pass

        cv2.imwrite(out_path,img)

    except Exception as e:
        print(in_path1,in_path,e)
print('done!!!!!!!!')