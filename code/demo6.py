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


def createCSV(pro,code): 
    #按性别分类
    M0 = d4.M0_func(pro)
    M1 = d4.M1_func(pro)
    M2 = d4.M2_func(pro)
    
    #按时间分类
    M0_C0 = d4.pro_func(M0)
    M0_C1 = d4.pro_func(d4.C1_func(M0))
    M1_C0 = d4.pro_func(M1)
    M1_C1 = d4.pro_func(d4.C1_func(M1))
    M2_C0 = d4.pro_func(M2)
    M2_C1 = d4.pro_func(d4.C1_func(M2))

    #数组处理共生成24个CSV文件
    M0_C0_S0 = d4.S0_func(code,M0_C0)
    M0_C0_S1 = d4.S1_func(code,M0_C0)
    M0_C0_S2 = d4.S2_func(code,M0_C0)
    M0_C0_S3 = d4.S3_func(code,M0_C0)
    
    M0_C1_S0 = d4.S0_func(code,M0_C1)
    M0_C1_S1 = d4.S1_func(code,M0_C1)
    M0_C1_S2 = d4.S2_func(code,M0_C1)
    M0_C1_S3 = d4.S3_func(code,M0_C1)
    
    M1_C0_S0 = d4.S0_func(code,M1_C0)
    M1_C0_S1 = d4.S1_func(code,M1_C0)
    M1_C0_S2 = d4.S2_func(code,M1_C0)
    M1_C0_S3 = d4.S3_func(code,M1_C0)
    
    M1_C1_S0 = d4.S0_func(code,M1_C1)
    M1_C1_S1 = d4.S1_func(code,M1_C1)
    M1_C1_S2 = d4.S2_func(code,M1_C1)
    M1_C1_S3 = d4.S3_func(code,M1_C1)
    
    M2_C0_S0 = d4.S0_func(code,M2_C0)
    M2_C0_S1 = d4.S1_func(code,M2_C0)
    M2_C0_S2 = d4.S2_func(code,M2_C0)
    M2_C0_S3 = d4.S3_func(code,M2_C0)
    
    M2_C1_S0 = d4.S0_func(code,M2_C1)
    M2_C1_S1 = d4.S1_func(code,M2_C1)
    M2_C1_S2 = d4.S2_func(code,M2_C1)
    M2_C1_S3 = d4.S3_func(code,M2_C1)
    result = [  M0_C0_S0,M0_C0_S1, M0_C0_S2, M0_C0_S3,
                  M0_C1_S0,M0_C1_S1, M0_C1_S2,M0_C1_S3,
                  M1_C0_S0,M1_C0_S1, M1_C0_S2,M1_C0_S3,
                  M1_C1_S0,M1_C1_S1, M1_C1_S2,M1_C1_S3,
                  M2_C0_S0,M2_C0_S1, M2_C0_S2,M2_C0_S3,
                  M2_C1_S0,M2_C1_S1, M2_C1_S2,M2_C1_S3]
    return result

'''
result1 = createCSV(d4.pro1,code1)
result2 = createCSV(d4.pro2,code2)
result3 = createCSV(d4.pro3,code3)
result4 = createCSV(d4.pro4,code4)
result5 = createCSV(d4.pro5,code5)


M0_C0_S0 = np.r_[result1[0],result2[0],result3[0],result4[0],result5[0]]
M0_C0_S1 = np.r_[result1[1],result2[1],result3[1],result4[1],result5[1]]
M0_C0_S2 = np.r_[result1[2],result2[2],result3[2],result4[2],result5[2]]
M0_C0_S3 = np.r_[result1[3],result2[3],result3[3],result4[3],result5[3]]
    
M0_C1_S0 = np.r_[result1[4],result2[4],result3[4],result4[4],result5[4]]
M0_C1_S1 = np.r_[result1[5],result2[5],result3[5],result4[5],result5[5]]
M0_C1_S2 = np.r_[result1[6],result2[6],result3[6],result4[6],result5[6]]
M0_C1_S3 = np.r_[result1[7],result2[7],result3[7],result4[7],result5[7]]
    
M1_C0_S0 = np.r_[result1[8],result2[8],result3[8],result4[8],result5[8]]
M1_C0_S1 = np.r_[result1[9],result2[9],result3[9],result4[9],result5[9]]
M1_C0_S2 = np.r_[result1[10],result2[10],result3[10],result4[10],result5[10]]
M1_C0_S3 = np.r_[result1[11],result2[11],result3[11],result4[11],result5[11]]
    
M1_C1_S0 = np.r_[result1[12],result2[12],result3[12],result4[12],result5[12]]
M1_C1_S1 = np.r_[result1[13],result2[13],result3[13],result4[13],result5[13]]
M1_C1_S2 = np.r_[result1[14],result2[14],result3[14],result4[14],result5[14]]
M1_C1_S3 = np.r_[result1[15],result2[15],result3[15],result4[15],result5[15]]
    
M2_C0_S0 = np.r_[result1[16],result2[16],result3[16],result4[16],result5[16]]
M2_C0_S1 = np.r_[result1[17],result2[17],result3[17],result4[17],result5[17]]
M2_C0_S2 = np.r_[result1[18],result2[18],result3[18],result4[18],result5[18]]
M2_C0_S3 = np.r_[result1[19],result2[19],result3[19],result4[19],result5[19]]
    
M2_C1_S0 = np.r_[result1[20],result2[20],result3[20],result4[20],result5[20]]
M2_C1_S1 = np.r_[result1[21],result2[21],result3[21],result4[21],result5[21]]
M2_C1_S2 = np.r_[result1[22],result2[22],result3[22],result4[22],result5[22]]
M2_C1_S3 = np.r_[result1[23],result2[23],result3[23],result4[23],result5[23]]


pd.DataFrame(M0_C0_S0,columns=d4.columns).to_csv('171110_P0_M0_A0_C0_S0.csv',index=False)
pd.DataFrame(M0_C0_S1,columns=d4.columns).to_csv('171110_P0_M0_A0_C0_S1.csv',index=False)
pd.DataFrame(M0_C0_S2,columns=d4.columns).to_csv('171110_P0_M0_A0_C0_S2.csv',index=False)
pd.DataFrame(M0_C0_S3,columns=d4.columns).to_csv('171110_P0_M0_A0_C0_S3.csv',index=False)

pd.DataFrame(M0_C1_S0,columns=d4.columns).to_csv('171110_P0_M0_A0_C1_S0.csv',index=False)
pd.DataFrame(M0_C1_S1,columns=d4.columns).to_csv('171110_P0_M0_A0_C1_S1.csv',index=False)
pd.DataFrame(M0_C1_S2,columns=d4.columns).to_csv('171110_P0_M0_A0_C1_S2.csv',index=False)
pd.DataFrame(M0_C1_S3,columns=d4.columns).to_csv('171110_P0_M0_A0_C1_S3.csv',index=False)

pd.DataFrame(M1_C0_S0,columns=d4.columns).to_csv('171110_P0_M1_A0_C0_S0.csv',index=False)
pd.DataFrame(M1_C0_S1,columns=d4.columns).to_csv('171110_P0_M1_A0_C0_S1.csv',index=False)
pd.DataFrame(M1_C0_S2,columns=d4.columns).to_csv('171110_P0_M1_A0_C0_S2.csv',index=False)
pd.DataFrame(M1_C0_S3,columns=d4.columns).to_csv('171110_P0_M1_A0_C0_S3.csv',index=False)

pd.DataFrame(M1_C1_S0,columns=d4.columns).to_csv('171110_P0_M1_A0_C1_S0.csv',index=False)
pd.DataFrame(M1_C1_S1,columns=d4.columns).to_csv('171110_P0_M1_A0_C1_S1.csv',index=False)
pd.DataFrame(M1_C1_S2,columns=d4.columns).to_csv('171110_P0_M1_A0_C1_S2.csv',index=False)
pd.DataFrame(M1_C1_S3,columns=d4.columns).to_csv('171110_P0_M1_A0_C1_S3.csv',index=False)

pd.DataFrame(M2_C0_S0,columns=d4.columns).to_csv('171110_P0_M2_A0_C0_S0.csv',index=False)
pd.DataFrame(M2_C0_S1,columns=d4.columns).to_csv('171110_P0_M2_A0_C0_S1.csv',index=False)
pd.DataFrame(M2_C0_S2,columns=d4.columns).to_csv('171110_P0_M2_A0_C0_S2.csv',index=False)
pd.DataFrame(M2_C0_S3,columns=d4.columns).to_csv('171110_P0_M2_A0_C0_S3.csv',index=False)

pd.DataFrame(M2_C1_S0,columns=d4.columns).to_csv('171110_P0_M2_A0_C1_S0.csv',index=False)
pd.DataFrame(M2_C1_S1,columns=d4.columns).to_csv('171110_P0_M2_A0_C1_S1.csv',index=False)
pd.DataFrame(M2_C1_S2,columns=d4.columns).to_csv('171110_P0_M2_A0_C1_S2.csv',index=False)
pd.DataFrame(M2_C1_S3,columns=d4.columns).to_csv('171110_P0_M2_A0_C1_S3.csv',index=False)
'''
