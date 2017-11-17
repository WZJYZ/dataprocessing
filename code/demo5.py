# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:53:54 2017

@author: lwj
"""

import numpy as np
import pandas as pd
import demo4 as d4


#所有的CSV数据
pro = np.r_[d4.pro1,d4.pro2,d4.pro3,d4.pro4,d4.pro5]
#从*.code生成np数组
code1 = d4.code_func(d4.code1)
code2 = d4.code_func(d4.code2)
code3 = d4.code_func(d4.code3)
code4 = d4.code_func(d4.code4)
code5 = d4.code_func(d4.code5)

code = np.r_[code1,code2,code3,code4,code5]

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

