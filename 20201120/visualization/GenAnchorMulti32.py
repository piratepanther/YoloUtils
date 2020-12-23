from os import listdir
from os.path import isfile, join
import argparse
#import cv2
import numpy as np
import sys
import os
import shutil
import random
import math

num_clusters=9

f = open('generated_anchors/anchors/anchors%d.txt' %num_clusters)
lines = [line.rstrip('\n') for line in f.readlines()]
lineNum=lines[0].split(',')
# map(lambda x: float(x)*2,lineNum)
# yan=map(lambda x: x*2,[2,3,4,5])
print(lineNum)
# print(yan)
# print(type(lineNum[0]))
for i in range(len(lineNum)):
    lineNum[i]=round(float(lineNum[i])*32)

print(lineNum)
f.close()