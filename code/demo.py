# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:32:04 2017

@author: lwj
"""

import numpy as np
import pandas as pd

code1 = np.loadtxt('../Juge/1.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
code2 = np.loadtxt('../Juge/2.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
code3 = np.loadtxt('../Juge/3.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
code4 = np.loadtxt('../Juge/4.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
code5 = np.loadtxt('../Juge/5.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)

pro1 = pd.read_csv('../Juge/1.csv',encoding='gbk')
pro2 = pd.read_csv('../Juge/2.csv',encoding='gbk')
pro3 = pd.read_csv('../Juge/3.csv',encoding='gbk')
pro4 = pd.read_csv('../Juge/4.csv',encoding='gbk')
pro5 = pd.read_csv('../Juge/5.csv',encoding='gbk')

def code_func(data):
    #生成3000*16的数组
    result = np.zeros((data.shape[0],17))
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

def pro_func(data):
    arr = data.values
    arr = arr[:,6:-2]
    return arr



'''
const = 0
for i in range(3000):
    #从*.csv中提取每道题的A/B值，1表示选A,2表示选B
    a = list()
    for j in pro_res1[:,i]:
        if j != -3:
            a.append(j)
    a = list(set(a))#对每个a中相同的1或2唯一化
    #填充A/B值，每道题中如果有人选A就在最后一列填1，否则填2，
    #如果既有选A也有选B，则把该道题复制一行，分别填1和2
    #
    if len(a) == 1:
        code_res1[const,-1] = a[0]
        const = const + 1
    elif len(a) == 2:
        code_res1 = np.insert(code_res1,const+1,code_res1[const,],axis=0)
        code_res1[const,-1] = a[0]
        code_res1[const+1,-1] = a[1]
        const = const + 2
    else:
        const = const + 1
    
'''
def all_func(code,pro):
    const = 0
    for i in range(3000):
        #从*.csv中提取每道题的A/B值，1表示选A,2表示选B
        a = list()
        for j in pro[:,i]:
            if j != -3:
                a.append(j)
        a = list(set(a))#对每个a中相同的1或2唯一化
        #填充A/B值，每道题中如果有人选A就在最后一列填1，否则填2，
        #如果既有选A也有选B，则把该道题复制一行，分别填1和2
        #
        if len(a) == 1:
            code[const,-1] = a[0]
            const = const + 1
        elif len(a) == 2:
            code = np.insert(code,const+1,code[const,],axis=0)
            code[const,-1] = a[0]
            code[const+1,-1] = a[1]
            const = const + 2
        else:
            code = np.delete(code,const,axis=0)
            #const = const + 1
    return code


#不做任何额外处理，若同一个问题有n个人回答，那么就保留n行
def S0_func(code,pro):
    const = 0
    for i in range(3000):
        #从*.csv中提取每道题的A/B值，1表示选A,2表示选B
        a = list()
        for j in pro[:,i]:
            if j != -3:
                a.append(j)
        
        if len(a)== 1:
            code[const,-1] = a[0]
            const = const + 1
        elif len(a)>1:
            row = code[const,]
            code[const,-1] = a[0]
            const = const + 1
            for k in a[1:]:
                code = np.insert(code,const,row,axis=0)
                code[const,-1] = k
                const = const + 1
        else:
            code = np.delete(code,const,axis=0)
            #const = const + 1
    return code


def S1_func(code,pro):
    const = 0
    for i in range(3000):
        #从*.csv中提取每道题的A/B值，1表示选A,2表示选B
        a = list()
        for j in pro[:,i]:
            if j != -3:
                a.append(j)
        if a.count(1) > a.count(2):
            code[const,-1] = 1
            const = const + 1
        elif a.count(1) < a.count(2):
            code[const,-1] = 2
            const = const + 1
        else:
            code = np.delete(code,const,axis=0)
    return code


def S2_func(code,pro):
    const = 0
    for i in range(3000):
        a = list()
        for j in pro[:,i]:
            if j != -3:
                a.append(j)
        if a.count(1) > a.count(2):
            code[const,-1] = 1
            const = const + 1
        elif a.count(1) < a.count(2):
            code[const,-1] = 2
            const = const + 1
        elif (a.count(1) == a.count(2))and (len(a)>0):
            code[const,-1] = 0
            const = const  + 1
        else:
            code = np.delete(code,const,axis=0)
    return code
            
def S3_func(code,pro):
    const = 0
    for i in range(3000):
        a = list()
        for j in pro[:,i]:
            if j != -3:
                a.append(j)
        if len(a)>0:
            n = a.count(1)
            m = a.count(2)
            p = m/(n+m)
            if 0<=p<0.2:
                code[const,-1] = 0
                const = const + 1
            if 0.2<=p<0.4:
                code[const,-1] = 1
                const = const + 1
            if 0.4<=p<0.6:
                code[const,-1] = 2
                const = const + 1
            if 0.6<=p<0.8:
                code[const,-1] = 3
                const = const + 1
            if 0.8<=p<=1:
                code[const,-1] = 4
                const = const + 1
        else:
             code = np.delete(code,const,axis=0)
    return code
                

code_res1 = code_func(code1)
#code_res2 = code_func(code2)
#code_res3 = code_func(code3)
#code_res4 = code_func(code4)
#code_res5 = code_func(code5)


pro_res1 = pro_func(pro1)
#pro_res2 = pro_func(pro2)
#pro_res3 = pro_func(pro3)
#pro_res4 = pro_func(pro4)
#pro_res5 = pro_func(pro5)

#data1 = all_func(code_res1,pro_res1)
#data2 = all_func(code_res2,pro_res2)
#data3 = all_func(code_res3,pro_res3)
#data4 = all_func(code_res4,pro_res4)
#data5 = all_func(code_res5,pro_res5)

#data = np.r_[data1,data2,data3,data4,data5]
#data = data.astype(np.int)
columns = ['A选项概率','0类型','1类型','2类型','3类型','4类型','5类型','6类型',
          'B选项概率','0类型','1类型','2类型','3类型','4类型','5类型','6类型','选A/B']

#pd.DataFrame(data,columns=columns).to_csv('data.csv',index=False)
#pd.DataFrame(code_res1).to_csv('demo.csv')

#data =S0_func(code_res1,pro_res1)
#pd.DataFrame(data,columns=columns).to_csv('data1.csv',index=False)  

#data =S1_func(code_res1,pro_res1)
#pd.DataFrame(data,columns=columns).to_csv('data2.csv',index=False)

#data =S2_func(code_res1,pro_res1)
#pd.DataFrame(data,columns=columns).to_csv('data3.csv',index=False)

data =S3_func(code_res1,pro_res1)
pd.DataFrame(data,columns=columns).to_csv('data4.csv',index=False)    
