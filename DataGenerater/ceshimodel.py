import cv2
import numpy as np
import random
# from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.externals import joblib


data=np.zeros(shape=(20,90000))
targetlist=[]
target_names=np.array([1,2])
for i in range(0,10):

    path="J:/data/20190122kaifeng/2st/biaozhun/zhendong/test/"+str(i+50)+".png"
    img = cv2.imread(path, 0)
    data[i,:]=img.reshape(1,img.size)
    targetlist = targetlist + [1]

for i in range(0,10):

    path="J:/data/20190122kaifeng/2st/biaozhun/gaotie/test/"+str(i+50)+".png"
    img = cv2.imread(path, 0)
    data[i+10,:]=img.reshape(1,img.size)
    targetlist = targetlist + [2]

target=np.array(targetlist)

# digits = {'data': data, 'target': target,'target_names':target_names}


ss = StandardScaler()


print(ss.fit_transform(data[1,:]))

data1 = ss.fit_transform(data)

clf = joblib.load("J:/data/20190122kaifeng/model/train_model_svc2.m")

target_y=clf.predict(data1)


print (target_y)
print ('The Accuracy of Linear SVC is', clf.score(data1, target))
print ('-----------------------------------------------------')
print (classification_report(target, target_y, target_names=target_names.astype(str)))