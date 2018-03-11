# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:09:41 2018

@author: lwj
"""

import os
import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC

def judge(test_Y,a):
    count = 0
    for i in range(len(a)):
        if a[i]==test_Y[i]:
            count += 1
    print(count/len(a))



data = list()
for filename in os.listdir("./data2"):#修改文件夹data，data2，data3
    data.append(pd.read_csv('./data2/' + filename ).values)

for i in range(len(data)):
    partition = int(len(data[i])*0.1)                 
    train_data = data[i][partition:,0:-1]
    train_Y = data[i][partition:,-1]
    test_data = data[i][0:partition,0:-1] 
    test_Y = data[i][0:partition,-1]
    
    clf = SVC(kernel='linear', decision_function_shape='ovo')
    clf.fit(train_data,train_Y)
    a = clf.predict(test_data)
    #print(a)

    judge(test_Y,a)