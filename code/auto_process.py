# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:13:53 2018

@author: lwj
"""
#2018-1-30 19:14
#自动化处理数据
import os
import os.path
import numpy as np
import pandas as pd
import predict as p1
import multiclass as m1
import multiclass2 as m2

data = list()
for filename in os.listdir("./data4"):#修改文件夹data，data2，data3
    data.append(pd.read_csv('./data4/' + filename ).values)

result = list()    
for i in range(len(data)):
    if i%4 == 0:
        partition = int(len(data[i])*9/10)
        w,v = p1.fit(data[i][0:partition,])
        p = p1.predict(w,data[i][partition:,])
        result.append([str(v),p])
        print("___S0——>"+ "训练集："+str(v)+"  测试集："+p)
    elif i%4 == 1:
        partition = int(len(data[i])*9/10)
        w,v = p1.fit(data[i][0:partition,])
        p = p1.predict(w,data[i][partition:,])
        result.append([str(v),p])
        print("___S1——>"+ "训练集："+str(v)+"  测试集："+p)
    elif i%4 == 2:
        partition = int(len(data[i])*9/10)
        w,v,t = m1.fit(data[i][0:partition,])
        p = m1.predict(w,data[i][partition:,],t)
        result.append([str(v),p])
        print("___S2——>"+ "训练集："+str(v)+"  测试集："+p)
    else:
        partition = int(len(data[i])*9/10)
        w,v,t1,t2 = m2.fit(data[i][0:partition,])
        p = m2.predict(w,data[i][partition:,],t1,t2)
        result.append([str(v),p])
        print("___S3——>"+ "训练集："+str(v)+"  测试集："+p)
    
#pd.DataFrame(result).to_csv('test.csv',index=False)