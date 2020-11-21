import numpy as np
import random
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.externals import joblib

# a=np.zeros((8,8))
# i=2
# j=3
# a[j:8, i:i+2]=1
# print(a)
# a=np.array(range(1,65)).reshape(8,8)
# print(a)
# print(a[3,7])
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
print(data.shape,target.shape,target)
# #数据分割
# X_train, X_test, y_train, y_test = train_test_split(digits['data'], digits['target'], test_size=0.25, random_state=33)
# #标准化
# ss = StandardScaler()
# X_train = ss.fit_transform(X_train)
# X_test = ss.transform(X_test)
#
# # 初始化线性假设的支持向量机分类器LinearSVC。
# lsvc = LinearSVC()
# #进行模型训练
# lsvc.fit(X_train, y_train)
# joblib.dump(lsvc, "J:/data/20190122kaifeng/model/train_model_svc.m")
# # 利用训练好的模型对测试样本的数字类别进行预测，预测结果储存在变量y_predict中。
# y_predict = lsvc.predict(X_test)
# # 使用模型自带的评估函数进行准确性测评。
# print ('The Accuracy of Linear SVC is', lsvc.score(X_test, y_test))
# print ('-----------------------------------------------------')
# # 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析。
# print (classification_report(y_test, y_predict, target_names=digits['target_names'].astype(str)))