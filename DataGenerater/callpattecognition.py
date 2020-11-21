# import sys
# sys.path.insert(0,"../")
# path="J:/data/20190122kaifeng/2st/12315141.png"
# # path="J:/data/20190122kaifeng/2st/biaozhun/zhendong/test/55.png"
# position=1300
# model="J:/data/20190122kaifeng/model/train_model_svc2.m"
import partternreco as pdd

# path="J:/data/20190122kaifeng/2st/biaozhun/zhendong/test/55.png"


path="J:/huarunranqi/2800mche/2800/2019-04-30-22-35-00.jpg"#1
position=1685#1

# path="J:/huarunranqi/watu/watu/2019-05-06-15-22-54.jpg"#2
# position=2338#2

model="J:/huarunranqi/biaozhun/model/train_model_svc1.m"
a=pdd.pattecognition(path,position,model)
print(a)


# pdd.pattecognition("J:/data/20190122kaifeng/2st/12315141.png",1300,"J:/data/20190122kaifeng/model/train_model_svc2.m")




