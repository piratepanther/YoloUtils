import numpy as np
import random
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.externals import joblib

datalist=[]
targetlist=[]   #1:b:ruqin,2:c:huoche,3:d:dafeng

#生成100组仿真数据
count = 0
for x in range(0,100):
    b = np.zeros((8, 8))
    d = np.zeros((8, 8))
    i = random.randint(1, 5)
    j = random.randint(0, 4)
    b[j:8, i:i + 2] = 1
    d[j:j+2, i:i + 2] = 1
    c=b.T
    b=b.reshape(1,64)
    c=c.reshape(1, 64)
    d = d.reshape(1, 64)
    b=b.tolist()
    c = c.tolist()
    d = d.tolist()
    # print(b,c,d)
    datalist=datalist+b+c+d
    targetlist=targetlist+[1,2,3]


#将数据转化成为nparray
data=np.array(datalist)
target=np.array(targetlist)
target_names=np.array([1,2,3])
digits = {'data': data, 'target': target,'target_names':target_names}
# print(digits)

ss = StandardScaler()

data1 = ss.fit_transform(data)

clf = joblib.load("J:/data/20190122kaifeng/model/train_model_svc.m")

target_y=clf.predict(data1)

print ('The Accuracy of Linear SVC is', clf.score(data1, target))
print ('-----------------------------------------------------')
print (classification_report(target, target_y, target_names=target_names.astype(str)))