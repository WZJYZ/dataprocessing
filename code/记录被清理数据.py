# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:34:23 2017

@author: lwj
"""
#记录时间小于60秒的数据
import numpy as np
import pandas as pd

data1 = pd.read_csv('../Juge/1.csv',encoding='gbk')
data2 = pd.read_csv('../Juge/2.csv',encoding='gbk')
data3 = pd.read_csv('../Juge/3.csv',encoding='gbk')
data4 = pd.read_csv('../Juge/4.csv',encoding='gbk')
data5 = pd.read_csv('../Juge/5.csv',encoding='gbk')


def C1_func(data):
    row = list()
    for i in range(data.shape[0]):
        if int(data[i,2][0:-1]) < 60:
            row.append(i+1)
    return row

res1 = {"1.csv":C1_func(data1.values)}
res2 = {"2.csv":C1_func(data2.values)}
res3 = {"3.csv":C1_func(data3.values)}
res4 = {"4.csv":C1_func(data4.values)}
res5 = {"5.csv":C1_func(data5.values)}
pd.Series(res1).to_csv("./record/res1.txt")
pd.Series(res2).to_csv("./record/res2.txt")
pd.Series(res3).to_csv("./record/res3.txt")
pd.Series(res4).to_csv("./record/res4.txt")
pd.Series(res5).to_csv("./record/res5.txt")
