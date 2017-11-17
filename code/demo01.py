# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:50:34 2017

@author: lwj
处理题目序号和值
"""
import numpy as np
import pandas as pd

data1 = pd.read_csv('../Juge/1.csv',encoding='gbk')
data2 = pd.read_csv('../Juge/2.csv',encoding='gbk')
data3 = pd.read_csv('../Juge/3.csv',encoding='gbk')
data4 = pd.read_csv('../Juge/4.csv',encoding='gbk')
data5 = pd.read_csv('../Juge/5.csv',encoding='gbk')


#返回每个文件的np数组
def resfunct(data):
    arr = data.values
    arr = arr[:,6:-2]
    result = np.argwhere(arr[0,:]>-3).T

    for i in range(1,arr.shape[0]):
        line = np.argwhere(arr[i,:]>-3).T
        result = np.row_stack((result,line))
    
    result = result + 1
    return result

'''  
result1 = resfunct(data1)
result2 = resfunct(data2)
result3 = resfunct(data3)
result4 = resfunct(data4)
result5 = resfunct(data5)

result = np.r_[result1,result2,result3,result4,result5]
title = ['题目1','题目2','题目3','题目4','题目5','题目6','题目7','题目8','题目9','题目10']
#problem = pd.DataFrame(result,columns=title)
#problem.to_csv('problem.csv',index=False)
'''



