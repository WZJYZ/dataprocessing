# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:43:27 2018

@author: lwj
"""

import numpy as np
import pandas as pd
import demo4 as d4

code_l = d4.code_func(d4.code_l)
code_y = d4.code_func(d4.code_y)

def S_func(code,pro):
    S0 = d4.S0_func(code,pro)
    S1 = d4.S1_func(code,pro)
    S2 = d4.S2_func(code,pro)
    S3 = d4.S3_func(code,pro)
    return S0,S1,S2,S3

def createCSV(code,pro):
    
    result = list()
    
    M0 = d4.M0_func(pro)
    
    M0_A0 = d4.A0_func(M0)
    
    M0_A0_C0 = d4.pro_func2(M0_A0)
    result.extend(S_func(code,M0_A0_C0))
    M0_A0_C1 = d4.pro_func2(d4.C1_func(M0_A0))
    result.extend(S_func(code,M0_A0_C1))
    M0_A0_C2 = d4.pro_func2(d4.C2_func(code,M0_A0))
    result.extend(S_func(code,M0_A0_C2))
    
    return result

def generateCSV(res,name):
    counter = 0
    for m in range(3):
        for n in range(4):
            pd.DataFrame(res[counter],columns=d4.columns).to_csv('./data3/'+name+'_171110_P0_M0_A0_C'+str(m)+'_S'+str(n)+'.csv',index=False)
            counter = counter + 1
    
    
result1 = createCSV(code_l,d4.pro_l)
result2 = createCSV(code_y,d4.pro_y)

generateCSV(result1,'LWJ')
generateCSV(result2,'YYP')