import cv2
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.externals import joblib
#imread,reshape,for i mat[:,i]=reshape, target=list[1,2,1,2,1,2,1,2,1]
data=np.zeros(shape=(120,2500))
targetlist=[]
target_names=np.array([1,2])
for i in range(0,60):

    path="J:/huarunranqi/biaozhun/guoche/"+str(i)+".jpg"
    img = cv2.imread(path, 0)
    data[i,:]=img.reshape(1,img.size)
    targetlist = targetlist + [1]

for i in range(0,60):

    path="J:/huarunranqi/biaozhun/watu/"+str(i)+".jpg"
    img = cv2.imread(path, 0)
    data[i+60,:]=img.reshape(1,img.size)
    targetlist = targetlist + [2]

target=np.array(targetlist)

digits = {'data': data, 'target': target,'target_names':target_names}
# print(digits)
# print(data.shape,target.shape)

#数据分割
X_train, X_test, y_train, y_test = train_test_split(digits['data'], digits['target'], test_size=0.25, random_state=33)
#标准化
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

# 初始化线性假设的支持向量机分类器LinearSVC。
lsvc = LinearSVC()
#进行模型训练
lsvc.fit(X_train, y_train)
joblib.dump(lsvc, "J:/huarunranqi/biaozhun/model/train_model_svc1.m")
# 利用训练好的模型对测试样本的数字类别进行预测，预测结果储存在变量y_predict中。
y_predict = lsvc.predict(X_test)
# 使用模型自带的评估函数进行准确性测评。
print ('The Accuracy of Linear SVC is', lsvc.score(X_test, y_test))
print ('-----------------------------------------------------')
# 依然使用sklearn.metrics里面的classification_report模块对预测结果做更加详细的分析。
print (classification_report(y_test, y_predict, target_names=digits['target_names'].astype(str)))







