# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 22:48:27 2017

@author: lwj
"""
#模拟退火算法
#w0...w8共九个权重值
import numpy as np
import pandas as pd
data1 = pd.read_csv("./171111_P0_M0_A0_C0_S0.csv").values
data2 = pd.read_csv("./171111_P0_M0_A0_C0_S1.csv").values      
partition = int(len(data1)*1/3)                 
train_data = data1[partition:,]
test_data = data1[0:partition,]                

#判断预测值和实际值是否匹配，计算概率

def judge(a,data):
    data = data[:,-1]
    count = 0;
    for i in range(len(a)):
        if a[i] == data[i]:
            count = count + 1
    return count/len(a)


#计算W和data乘积，比较Y1，Y2，生成数组a
#W:权重数组
#data：数据集

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

#接受准则
def accept(delta,t):
    if (delta > 0) or (np.math.exp(delta/t) > np.random.rand()):
        return True
    


                             


def fit(train_data):
    T_min = 1e-3
    W = np.random.rand(9)
    old_value = judge(get_a(W,train_data),train_data)
    T = 100
    while T > T_min:
        for i in range(10):
            new_W = W
            n = np.random.randint(0,9)
            new_W[n] = np.random.rand()
            new_value = judge(get_a(new_W,train_data),train_data)
            delta = new_value - old_value
            if accept(delta,T):
                W = new_W
                old_value = new_value
            print(old_value)
        T = T*0.98
       
    return W


def predict(test_data,W):
    print("predict_data:"+str(judge(get_a(W,test_data),test_data)))
    
'''
if __name__ == "__main__":
    for i in range(5):
        W = fit(train_data)
        predict(test_data,W)
'''
