import numpy as np
import cv2
import random
import time




img=np.zeros((20,20,1), np.uint8)

# in_path='J:/HRImage/20201214imageprocess/todo/tieqiu/'+str("%05d" % randnum)+'.jpg'
in_path = 'J:/HRImage/20201214imageprocess/todo/tieqiu/1-000001.jpg'
out_path='J:/HRImage/20201214imageprocess/done/1.jpg'

img4 = cv2.imread(in_path,0)

# img3 = cv2.applyColorMap(img, cv2.COLORMAP_JET)
# if(img4.shape[0] and img4.shape[1]):
try:
    x1=random.randint(1,20-img4.shape[0])
    y1=random.randint(1,20-img4.shape[1])
    for i in range(img4.shape[0]):
     for j in range(img4.shape[1]):
      img[i+x1][j+y1] = img4[i][j]

    cv2.imwrite(out_path,img)
        # time.sleep(0.1)
    # else:
    #     pass
except:
    print(in_path)

