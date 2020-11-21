import numpy as np
import cv2
import random
import time

totalnum=4000

for z in range(3000):

    in_path='J:/data/yolo/todo/retodo/strike/'+str("%05d" % z)+'.jpg'
    out_path='J:/data/yolo/todo/retodo/all/'+str("%05d" % (z+totalnum))+'.jpg'

    img4 = cv2.imread(in_path,1)

    try:

        cv2.imwrite(out_path,img4)
            # time.sleep(0.1)
        # else:
        #     pass
    except:
        print(in_path)
