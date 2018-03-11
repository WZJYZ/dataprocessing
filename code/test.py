# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 23:23:53 2017

@author: lwj
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
data1 = pd.read_csv("./data/171110_P0_M0_A0_C0_S0.csv").values
data2 = pd.read_csv("./data/171110_P0_M0_A0_C0_S1.csv").values
data3 = pd.read_csv("./data/171110_P0_M0_A0_C0_S2.csv").values                   
data4 = pd.read_csv("./data/171110_P0_M0_A0_C0_S3.csv").values                   
partition = int(len(data2)*1/10)                 
train_data = data2[partition:,0:-1]
train_Y = data2[partition:,-1]
test_data = data2[0:partition,0:-1] 
test_Y = data2[0:partition,-1] 

def judge(test_Y,a):
    count = 0
    for i in range(len(a)):
        if a[i]==test_Y[i]:
            count += 1
    print(count/len(a))

clf = SVC()
clf.fit(train_data,train_Y)
a = clf.predict(test_data)
print(a)

judge(test_Y,a)


            
    