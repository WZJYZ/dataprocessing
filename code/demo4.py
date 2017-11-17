# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:00:25 2017

@author: lwj
"""

import numpy as np
import pandas as pd

#获取文件
code1 = np.loadtxt('../Juge/1.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
code2 = np.loadtxt('../Juge/2.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
code3 = np.loadtxt('../Juge/3.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
code4 = np.loadtxt('../Juge/4.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)
code5 = np.loadtxt('../Juge/5.code',skiprows=1,delimiter='  ',dtype=bytes,usecols=(1,2)).astype(str)

pro1 = pd.read_csv('../Juge/1.csv',encoding='gbk').values
pro2 = pd.read_csv('../Juge/2.csv',encoding='gbk').values
pro3 = pd.read_csv('../Juge/3.csv',encoding='gbk').values
pro4 = pd.read_csv('../Juge/4.csv',encoding='gbk').values
pro5 = pd.read_csv('../Juge/5.csv',encoding='gbk').values

#data标题
columns = ['A选项概率','A选项人数','0类型','1类型','2类型','3类型','4类型','5类型','6类型',
          'B选项概率','B选项人数','0类型','1类型','2类型','3类型','4类型','5类型','6类型','选A/B']


#获取*.CSV中3000道题的数组
#data：pro1...pro5
def pro_func(data):
    data = data[:,6:-2]
    return data

#从*.code中生成数组
#data:code1...code5
def code_func(data):
    #生成3000*19的数组
    result = np.zeros((data.shape[0],19))
    for i in range(data.shape[0]):
        result[i,0] = data[i,0].replace(' ','')[0]
        result[i,1] = data[i,0].replace(' ','')[1]
        result[i,9] = data[i,1].replace(' ','')[0]
        result[i,10] = data[i,1].replace(' ','')[1]
        num1 = pd.value_counts(list(data[i,0].replace(' ','')[2:]))
        num2 = pd.value_counts(list(data[i,1].replace(' ','')[2:]))
        for j in num1.index:
            result[i,int(j)+2] = num1[j]
        for j in num2.index:
            result[i,int(j)+10] = num2[j]
    
    return result

#第一步：按省份划分，所有省份，既不处理
#第二部：按性别划分M0,M1,M2
#提取所有性别的数据
def M0_func(data):
    return data
#提取性别为1的数据
def M1_func(data):
    row = list()
    for i in range(data.shape[0]):
        if data[i,-2] == 2:
           row.append(i) #性别为2的列表组合
    return np.delete(data,row,axis=0)        
#提取性别为2的数据
def M2_func(data):
    row = list()
    for i in range(data.shape[0]):
        if data[i,-2] == 1:
           row.append(i) #性别为1的列表组合
    return np.delete(data,row,axis=0)

#第三步：按年龄划分，所有年龄即不划分
#第四步：对时间进行处理，C0不做任何处理，C1剔除时间<60秒的数据
def C1_func(data):
    row = list()
    for i in range(data.shape[0]):
        if int(data[i,2][0:-1]) < 60:
            row.append(i)
    return np.delete(data,row,axis=0)


#第五步：数据处理，S0,S1,S2,S3
#S0:不做任何处理

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







#测试code生成的数组
#pd.DataFrame(code_func(code1).astype(int),columns=columns).to_csv('test.csv')
#测试性别处理
#pd.DataFrame(M1_func(pro1)).to_csv('test2.csv')

#测试时间>=60秒的处理
#pd.DataFrame(C1_func(pro1).astype(str)).to_csv('test1.csv')