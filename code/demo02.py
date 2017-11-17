# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 22:18:16 2017

@author: lwj
处理.csv文件，生成每个人信息的np数组
"""

import pandas as pd 
import numpy as np
data1 = pd.read_csv('../Juge/1.csv',encoding='gbk')
data2 = pd.read_csv('../Juge/2.csv',encoding='gbk')
data3 = pd.read_csv('../Juge/3.csv',encoding='gbk')
data4 = pd.read_csv('../Juge/4.csv',encoding='gbk')
data5 = pd.read_csv('../Juge/5.csv',encoding='gbk')

 
def arrfunc(data):
    arr = data[[1,2,3,-2,-1]].values
    #获取提交时间（小时h）和所用时间（秒s）
    for i in range(arr.shape[0]):
        arr[i,0] = arr[i,0].split(' ')[1].split(':')[0]
        arr[i,1] = arr[i,1][:-1]
    #插入一列空列，值为0，用来保存省会
    arr = np.insert(arr,3,0,axis=1)
    #获取IP地址和省会
    for i in range(arr.shape[0]):
        arr[i,2],arr[i,3] = arr[i,2].split('(')
        arr[i,3] = arr[i,3].split('-')[0]
    return arr



arr1 = arrfunc(data1)
arr2 = arrfunc(data2)
arr3 = arrfunc(data3)
arr4 = arrfunc(data4)
arr5 = arrfunc(data5)
arr = np.r_[arr1,arr2,arr3,arr4,arr5]

title = ['提交时间(h)','所用时间(s)','IP地址','省会','性别','年龄']
person = pd.DataFrame(arr,columns=title)
person.to_csv('person.csv',index=False)





























