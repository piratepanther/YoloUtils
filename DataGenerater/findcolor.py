import numpy as np
import cv2
import random
import time
img=np.zeros((608,608,3), np.uint8)
#totalnum=1827
totalnum=20
for z in range(totalnum):

    in_path='J:/data/yolo/todo/todo/wind/'+str("%05d" % z)+'.jpg'


    img4 = cv2.imread(in_path,1)

    #[128, 0, 1]
    # if(img4.shape[0] and img4.shape[1]):
    try:
        a=(img4[1][1] == [128, 0, 1]).all()
        # print(not a)
        if (not a):
            print(in_path,img4[1][1])

            # time.sleep(0.1)
        # else:
        #     pass

    except Exception as e:
        print('///////' + in_path + '///////')
        print(e)