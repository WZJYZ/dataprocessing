# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:41:23 2017

@author: lwj
"""

import numpy as np
import pandas as pd
import demo4 as d4

code1 = d4.code_func(d4.code1)
code2 = d4.code_func(d4.code2)
code3 = d4.code_func(d4.code3)
code4 = d4.code_func(d4.code4)
code5 = d4.code_func(d4.code5)

def S_func(code,pro):
    S0 = d4.S0_func(code,pro)
    S1 = d4.S1_func(code,pro)
    S2 = d4.S2_func(code,pro)
    S3 = d4.S3_func(code,pro)
    return S0,S1,S2,S3

def createCSV(pro,code): 
    result = list()
    #按性别分类
    M0 = d4.M0_func(pro)
    M1 = d4.M1_func(pro)
    M2 = d4.M2_func(pro)
    #按年龄段分类
    M0_A0 = d4.A0_func(M0)
    M0_A1 = d4.A1_func(M0)
    M0_A2 = d4.A2_func(M0)
    
    M1_A0 = d4.A0_func(M1)
    M1_A1 = d4.A1_func(M1)
    M1_A2 = d4.A2_func(M1)
    
    M2_A0 = d4.A0_func(M2)
    M2_A1 = d4.A1_func(M2)
    M2_A2 = d4.A2_func(M2)
    #按时间分类
    M0_A0_C0 = d4.pro_func(M0_A0)
    result.extend(S_func(code,M0_A0_C0))
    M0_A0_C1 = d4.pro_func(d4.C1_func(M0_A0))
    result.extend(S_func(code,M0_A0_C1))
    M0_A0_C2 = d4.pro_func(d4.C2_func(code,M0_A0))
    result.extend(S_func(code,M0_A0_C2))
    M0_A1_C0 = d4.pro_func(M0_A1)
    result.extend(S_func(code,M0_A1_C0))
    M0_A1_C1 = d4.pro_func(d4.C1_func(M0_A1))
    result.extend(S_func(code,M0_A1_C1))
    M0_A1_C2 = d4.pro_func(d4.C2_func(code,M0_A1))
    result.extend(S_func(code,M0_A1_C2))
    M0_A2_C0 = d4.pro_func(M0_A2)
    result.extend(S_func(code,M0_A2_C0))
    M0_A2_C1 = d4.pro_func(d4.C1_func(M0_A2))
    result.extend(S_func(code,M0_A2_C1))
    M0_A2_C2 = d4.pro_func(d4.C2_func(code,M0_A2))
    result.extend(S_func(code,M0_A2_C2))
    
    M1_A0_C0 = d4.pro_func(M1_A0)
    result.extend(S_func(code,M1_A0_C0))
    M1_A0_C1 = d4.pro_func(d4.C1_func(M1_A0))
    result.extend(S_func(code,M1_A0_C1))
    M1_A0_C2 = d4.pro_func(d4.C2_func(code,M1_A0))
    result.extend(S_func(code,M1_A0_C2))
    M1_A1_C0 = d4.pro_func(M1_A1)
    result.extend(S_func(code,M1_A1_C0))
    M1_A1_C1 = d4.pro_func(d4.C1_func(M1_A1))
    result.extend(S_func(code,M1_A1_C1))
    M1_A1_C2 = d4.pro_func(d4.C2_func(code,M1_A1))
    result.extend(S_func(code,M1_A1_C2))
    M1_A2_C0 = d4.pro_func(M1_A2)
    result.extend(S_func(code,M1_A2_C0))
    M1_A2_C1 = d4.pro_func(d4.C1_func(M1_A2))
    result.extend(S_func(code,M1_A2_C1))
    M1_A2_C2 = d4.pro_func(d4.C2_func(code,M1_A2))
    result.extend(S_func(code,M1_A2_C2))
    
    M2_A0_C0 = d4.pro_func(M2_A0)
    result.extend(S_func(code,M2_A0_C0))
    M2_A0_C1 = d4.pro_func(d4.C1_func(M2_A0))
    result.extend(S_func(code,M2_A0_C1))
    M2_A0_C2 = d4.pro_func(d4.C2_func(code,M2_A0))
    result.extend(S_func(code,M2_A0_C2))
    M2_A1_C0 = d4.pro_func(M2_A1)
    result.extend(S_func(code,M2_A1_C0))
    M2_A1_C1 = d4.pro_func(d4.C1_func(M2_A1))
    result.extend(S_func(code,M2_A1_C1))
    M2_A1_C2 = d4.pro_func(d4.C2_func(code, M2_A1))
    result.extend(S_func(code,M2_A1_C2))
    M2_A2_C0 = d4.pro_func(M2_A2)
    result.extend(S_func(code,M2_A2_C0))
    M2_A2_C1 = d4.pro_func(d4.C1_func(M2_A2))
    result.extend(S_func(code,M2_A2_C1))
    M2_A2_C2 = d4.pro_func(d4.C2_func(code,M2_A2))
    result.extend(S_func(code,M2_A2_C2))

    #数组处理共生成24个CSV文件
    
    return result


result1 = createCSV(d4.pro1,code1)
result2 = createCSV(d4.pro2,code2)
result3 = createCSV(d4.pro3,code3)
result4 = createCSV(d4.pro4,code4)
result5 = createCSV(d4.pro5,code5)

res = list()
for i in range(len(result1)):
    temp = np.r_[result1[i],result2[i],result3[i],result4[i],result5[i]]
    res.append(temp)

counter = 0
for i in range(3):
    for j in range(3):
        for m in range(3):
            for n in range(4):
                pd.DataFrame(res[counter],columns=d4.columns).to_csv('./data2/171110_P0'+'_M'+str(i)+'_A'+str(j)+'_C'+str(m)+'_S'+str(n)+'.csv',index=False)
                counter = counter + 1
'''
pd.DataFrame(M0_C0_S0,columns=d4.columns).to_csv('171110_P0_M0_A0_C0_S0.csv',index=False)
'''

