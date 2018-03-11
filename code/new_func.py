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
import os
import os.path
import numpy as np
import pandas as pd



data1 = pd.read_csv("./data2/171110_P0_M0_A0_C0_S0.csv",dtype=np.int).values
data2 = pd.read_csv("./data2/171110_P0_M0_A0_C0_S1.csv",dtype=np.int).values      
partition1 = int(len(data1)*0.1)                 
train_data1 = data1[partition1:,]
test_data1 = data1[0:partition1,] 
partition2 = int(len(data2)*0.1)                 
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
        Y1 = W[t1-4].dot(data[i,][1:9])
        Y2 = W[t2-4].dot(data[i,][10:-1])
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
    T_init = 100 #初始温度
    T_min = 1e-5    #最小温度
    alpha = 0.99 #每次降温系数
    T = T_init #初始化温度
    W =  list()
    for i in range(4):
        temp = np.random.rand(8)
        W.append(temp)
    old_value = judge(W,train_data)
    while T > T_min:
        n = np.random.randint(0,8)
        W_new = W.copy()
        for i in range(4):
            W_new[i][n] = np.random.rand()
        new_value = judge(W_new,train_data)
        if new_value>old_value or np.math.exp(-(old_value-new_value)/T)>np.random.rand():
            W = W_new.copy()
            old_value = new_value
            
        T = T*alpha
    return W,old_value

def predict(W,test_data):
    #print("predict_data:"+str(judge(W,test_data)))
    return str(judge(W,test_data))
    




data = list()
for filename in os.listdir("./data2"):#修改文件夹data，data2，data3
    data.append(pd.read_csv('./data2/' + filename,dtype=np.int ).values)

result = list()
for i in range(len(data)):
    if i%4 == 0:
        partition = int(len(data[i])*0.9)
        w,v = fit(data[i][0:partition,])
        p = predict(w,data[i][partition:,])
        print("___S0——>"+ "训练集："+str(v)+"  测试集："+p)
        result.append([str(v),p])
    elif i%4 == 1:
        partition = int(len(data[i])*0.9)
        w,v = fit(data[i][0:partition,])
        p = predict(w,data[i][partition:,])
        print("___S1——>"+ "训练集："+str(v)+"  测试集："+p)
        result.append([str(v),p])
    elif i%4 == 2:
        result.append(['0','0'])
    else:
        result.append(['0','0'])
        
    



