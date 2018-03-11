# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 22:48:27 2017

@author: lwj
"""
#模拟退火算法
#w0...w8共九个权重值
import numpy as np
import pandas as pd


data1 = pd.read_csv("./data4/171110_P0_M0_A0_C0_S0.csv").values
data2 = pd.read_csv("./data4/171110_P0_M0_A0_C0_S1.csv").values      
partition1 = int(len(data1)*1/10)                 
train_data1 = data1[partition1:,]
test_data1 = data1[0:partition1,] 
partition2 = int(len(data2)*1/10)                 
train_data2 = data2[partition2:,]
test_data2 = data2[0:partition2,]

#计算W和data乘积，比较Y1，Y2，生成数组a
#W:权重数组
#data：数据集
'''
def get_a(W,data):
    a = list()
    for i in range(len(data)):
        Y1 = W.dot(data[i,][0:9])
        Y2 = W.dot(data[i,][9:-1])
        if Y1 > Y2:
            a.append(1)
        else:
            a.append(2)
    return a

def get_a(W,data):
    a = list()
    for i in range(len(data)):
        Y1 = W[1:9].dot(data[i,][1:9])+(W[0]*data[i,][0])**2
        Y2 = W[1:9].dot(data[i,][10:-1])+(W[0]*data[i,][9])**2
        if Y1 > Y2:
            a.append(1)
        else:
            a.append(2)
    return a
'''
def get_a(W,data):
    a = list()
    for i in range(len(data)):
        Y1 = W[2:9].dot(data[i,][2:9])
        Y2 = W[2:9].dot(data[i,][11:-1])
        if ((data[i,][0]>data[i,][11])and())or(Y1 > Y2):
            a.append(1)
        else:
            a.append(2)
    return a             

#判断预测值和实际值是否匹配，计算概率

def judge(W,data):
    a = get_a(W,data)
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
    old_value = judge(W,train_data)
    #value = [old_value]
    #best_W = W.copy() 
    while T > T_min:
        n = np.random.randint(0,9)
        W_new = W.copy()
        W_new[n] = np.random.rand()
        new_value = judge(W_new,train_data)
        if new_value>old_value or np.math.exp(-(old_value-new_value)/T)>np.random.rand():
            W = W_new.copy()
            old_value = new_value
           # best_W = W.copy()
        T = T*alpha
        #value.append(old_value)
    #print("二类value:"+str(old_value))
    return W,old_value 




def predict(W,test_data):
    #print("  predict_data:"+str(judge(W,test_data)))
    return str(judge(W,test_data))
    

w1,v1 = fit(train_data1)
t1 = predict(w1,test_data1)
print("训练集："+str(v1)+"  测试集："+str(t1))
w2,v2 = fit(train_data2)
t2 = predict(w2,test_data2)
print("训练集："+str(v2)+"  测试集："+str(t2))
    
    

