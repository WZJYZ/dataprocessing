# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:37:55 2018

@author: lwj
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 22:48:27 2017

@author: lwj
"""
#模拟退火算法
#w0...w8共九个权重值
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data1 = pd.read_csv("./data/171111_P0_M0_A0_C0_S0.csv",dtype=np.int).values
data2 = pd.read_csv("./data/171111_P0_M2_A0_C1_S1.csv").values      
partition1 = int(len(data1)*1/10)                 
train_data1 = data1[partition1:,]
test_data1 = data1[0:partition1,] 
partition2 = int(len(data2)*1/10)                 
train_data2 = data2[partition2:,]
test_data2 = data2[0:partition2,]

#计算W和data乘积，比较Y1，Y2，生成数组a
#W:权重数组
#data：数据集
#4 W[0],5 W[1],6 W[2],7 W[3]
def get_a(W,data):
    a = list()
    for i in range(len(data)):
        t1 = data[i,][0]
        t2 = data[i,][9]
        temp_W1 = W[t1-4]
        temp_W2 = W[t2-4]
        Y1 = temp_W1.dot(data[i,][2:9])
        Y2 = temp_W2.dot(data[i,][11:-1])
        if Y1 > Y2:
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
    T_init = 1000 #初始温度
    T_min = 1e-5    #最小温度
    alpha = 0.99 #每次降温系数
    T = T_init #初始化温度
    W =  list()
    for i in range(4):
        temp = np.random.rand(7)
        W.append(temp)
    old_value = judge(W,train_data)
    value = [old_value]
    #best_W = W.copy() 
    while T > T_min:
        n = np.random.randint(0,7)
        W_new = W.copy()
        for i in range(4):
            W_new[i][n] = np.random.rand()
        new_value = judge(W_new,train_data)
        if new_value>old_value or np.math.exp(-(old_value-new_value)/T)>np.random.rand():
            W = W_new.copy()
            old_value = new_value
           # best_W = W.copy()
        T = T*alpha
        value.append(old_value)
        print("value:"+str(old_value))
    return W,value 

def predict(W,test_data):
    print("predict_data:"+str(judge(W,test_data)))
    
    

def show(value):
    plt.ylim(0,1)
    plt.plot(value)
    
    
'''
if __name__ == "__main__":
    for i in range(5):
        W = fit(train_data)
        predict(test_data,W)
'''

