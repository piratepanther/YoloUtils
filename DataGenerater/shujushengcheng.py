import numpy as np
import cv2
import random
import time
img=np.zeros((608,608,3), np.uint8)
totalnum=1827

for z in range(3000):

    randnum = random.randint(0, totalnum)
    in_path='J:/data/yolo/todo/todo/wind/'+str("%05d" % randnum)+'.jpg'
    out_path='J:/data/yolo/todo/retodo/wind/'+str("%05d" % z)+'.jpg'

    img4 = cv2.imread(in_path,1)

    img3 = cv2.applyColorMap(img, cv2.COLORMAP_JET)
    # if(img4.shape[0] and img4.shape[1]):
    try:
        x=random.randint(1,608-img4.shape[0])
        y=random.randint(1,608-img4.shape[1])
        for i in range(img4.shape[0]):
         for j in range(img4.shape[1]):
          img3[i+x][j+y] = img4[i][j]

        cv2.imwrite(out_path,img3)
            # time.sleep(0.1)
        # else:
        #     pass
    except:
        print(in_path)
