import cv2
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib

# path="J:/data/20190122kaifeng/2st/1231597.png"
# # path="J:/data/20190122kaifeng/2st/biaozhun/zhendong/test/55.png"
# position=280
# model="J:/data/20190122kaifeng/model/train_model_svc2.m"

def pattecognition(path,position,model):
    step_column = 25

    data = np.zeros(shape=(41, 2500))

    for i in range(0, 20):
        path1 = "J:/huarunranqi/biaozhun/guoche/test/" + str(i + 60) + ".jpg"
        img = cv2.imread(path1, 0)
        data[i, :] = img.reshape(1, img.size)

    for i in range(0, 20):
        path1 = "J:/huarunranqi/biaozhun/watu/test/" + str(i + 60) + ".jpg"
        img = cv2.imread(path1, 0)
        data[i + 20, :] = img.reshape(1, img.size)

    img = cv2.imread(path, 0)

    img2 = img[0:50, position - step_column:position + step_column]

    data[40, :] = img2.reshape(1, img2.size)

    # data[20, :] = img.reshape(1, img.size)

    ss = StandardScaler()

    data1 = ss.fit_transform(data)

    clf = joblib.load(model)

    target_y = clf.predict(data1)

    # print(target_y)

    return target_y[40]


# print(pattecognition(path,position,model))