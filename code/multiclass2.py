# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 22:48:27 2017

@author: lwj
"""
#多分类任务之S3：五个类别0,1,2,3,4
#模拟退火算法
#w0...w8共九个权重值
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
data1 = pd.read_csv("./data/171111_P0_M0_A0_C0_S3.csv").values
partition1 = int(len(data1)*1/10)                 
train_data1 = data1[partition1:,]
test_data1 = data1[0:partition1,] 
'''

#计算W和data乘积，比较Y1，Y2，生成数组a
#W:权重数组
#data：数据集
#t1,t2:阈值
def get_a(W, data, t1,t2):
    max_t = 0
    min_t = 0
    if t1 >= t2:
        max_t = t1
        min_t = t2
    else:
        max_t = t2
        min_t = t1
    a = list()
    for i in range(len(data)):
        Y1 = W.dot(data[i,][0:9])
        Y2 = W.dot(data[i,][9:-1])
        delta = Y1 - Y2 
        if delta >= max_t:
            a.append(0)
        elif min_t <= delta < max_t:
            a.append(1)
        elif -min_t <= delta < min_t:
            a.append(2)
        elif -max_t <= delta < -min_t:
            a.append(3)
        else:
            a.append(4)
    return a


               

#判断预测值和实际值是否匹配，计算概率

def judge(W,data,t1,t2):
    a = get_a(W,data,t1,t2)
    data = data[:,-1]
    count = 0;
    for i in range(len(a)):
        if a[i] == data[i]:
            count = count + 1
    return count/len(a)




#接受准则
def accept(delta,t):
    if (delta > 0) or (np.math.exp(delta/t) > np.random.rand()):
        return True
    


                             
 

def fit(train_data):
    T_init = 100 #初始温度
    T_min = 1e-5    #最小温度
    alpha = 0.99 #每次降温系数
    T = T_init #初始化温度
    W = np.random.rand(9)
    threshold1 = np.random.rand()
    threshold2 = np.random.rand()
    old_value = judge(W,train_data,threshold1,threshold2)
    #value = [old_value]
    #best_W = W.copy() 
    while T > T_min:
        n = np.random.randint(0,9)
        W_new = W.copy()
        W_new[n] = np.random.rand()
        new_threshold1 = np.random.rand()
        new_threshold2 = np.random.rand()
        new_value = judge(W_new,train_data,new_threshold1,new_threshold2)
        if new_value>old_value or np.math.exp(-(old_value-new_value)/T)>np.random.rand():
            W = W_new.copy()
            old_value = new_value
            threshold1 = new_threshold1
            threshold2 = new_threshold2
           # best_W = W.copy()
        T = T*alpha
        #value.append(old_value)
    #print("五类value:"+str(old_value))
    return W,old_value,threshold1,threshold2 

def predict(W,test_data,t1,t2):
    #print("  predict_data:"+str(judge(W,test_data,t1,t2)))
    return str(judge(W,test_data,t1,t2))
    

def show(value):
    plt.ylim(0,1)
    plt.plot(value)
    
    
'''
if __name__ == "__main__":
    for i in range(5):
        W = fit(train_data)
        predict(test_data,W)
'''
