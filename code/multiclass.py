# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 22:48:27 2017

@author: lwj
"""
#多分类任务之S2：三个类别0,1,2
#模拟退火算法
#w0...w8共九个权重值
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./data/171110_P0_M1_A0_C1_S2.csv").values
partition = int(len(data)*1/10)                 
train_data = data[partition:,]
test_data = data[0:partition,] 


#计算W和data乘积，比较Y1，Y2，生成数组a
#W:权重数组
#data：数据集

def get_a(W, data, t):
    a = list()
    for i in range(len(data)):
        Y1 = W.dot(data[i,][0:9])
        Y2 = W.dot(data[i,][9:-1])
        delta = Y1 - Y2 
        if delta >= t:
            a.append(1)
        elif delta < -t:
            a.append(2)
        else:
            a.append(0)
    return a


               

#判断预测值和实际值是否匹配，计算概率

def judge(W,data,t):
    a = get_a(W,data,t)
    data = data[:,-1]
    count = 0;
    for i in range(len(a)):
        if a[i] == data[i]:
            count = count + 1
    return count/len(a)






                             
#训练
#train_data:训练数据 

def fit(train_data):
    T_init = 100 #初始温度
    T_min = 1e-5    #最小温度
    alpha = 0.99 #每次降温系数
    T = T_init #初始化温度
    W = np.random.rand(9)
    threshold = np.random.rand()
    old_value = judge(W,train_data,threshold)
    #value = [old_value]
    #best_W = W.copy() 
    while T > T_min:
        n = np.random.randint(0,9)
        W_new = W.copy()
        W_new[n] = np.random.rand()
        new_threshold = np.random.rand()
        new_value = judge(W_new,train_data,new_threshold)
        if new_value>old_value or np.math.exp(-(old_value-new_value)/T)>np.random.rand():
            W = W_new.copy()
            old_value = new_value
            threshold = new_threshold
           # best_W = W.copy()
        T = T*alpha
        #value.append(old_value)
        #print("三类value:"+str(old_value))
    return W,old_value,threshold 
#测试
#W：训练获得的参数
#test_data:测试数据
#t:阈值
def predict(W,test_data,t):
    #print("  predict_data:"+str(judge(W,test_data,t)))
    return str(judge(W,test_data,t))
    



