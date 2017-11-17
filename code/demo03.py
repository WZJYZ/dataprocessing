# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 22:18:16 2017

@author: lwj
处理.code文件，生成np数组
"""

import numpy as np
import pandas as pd

#file = open('../Juge/1.code','r')
#file.readline()

data1 = np.loadtxt('../Juge/1.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
data2 = np.loadtxt('../Juge/2.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
data3 = np.loadtxt('../Juge/3.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
data4 = np.loadtxt('../Juge/4.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
data5 = np.loadtxt('../Juge/5.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
    
columns = ['A选项概率','0类型','1类型','2类型','3类型','4类型','5类型','6类型',
          'B选项概率','0类型','1类型','2类型','3类型','4类型','5类型','6类型']

def func(data):
    #生成3000*16的数组
    result = np.zeros((data1.shape[0],16))
    for i in range(data.shape[0]):
        result[i,0] = data[i,0].replace(' ','')[0]
        result[i,8] = data[i,1].replace(' ','')[0]
        num1 = pd.value_counts(list(data[i,0].replace(' ','')[2:]))
        num2 = pd.value_counts(list(data[i,1].replace(' ','')[2:]))
        for j in num1.index:
            result[i,int(j)+1] = num1[j]
        for j in num2.index:
            result[i,int(j)+9] = num2[j]
    
    return result

result1 = func(data1)
result2 = func(data2)
result3 = func(data3)
result4 = func(data4)
result5 = func(data5)
'''
result = np.r_[result1,result2,result3,result4,result5]
code = pd.DataFrame(result.astype(int),columns=columns)
code.to_csv('code.csv',index=False)
'''







    
