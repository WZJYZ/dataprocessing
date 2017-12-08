# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:57:53 2017

@author: lwj
"""

'''
a = list()
for i in range(5000):
    Y1 = W.dot(data[i,][0:9])
    Y2 = W.dot(data[i,][9:-1])
    if Y1 > Y2:
        a.append(1)
    else:
        a.append(2)



#训练
def fit():
    W = np.random.rand(9)
    #print(judge(a,data[0:5000,-1]))
    T = 100
    T_min = 1e-8
    #随机替换W中一个数
    t = T
    while t > 89:
        for i in range(100):
            #old_W = W
            old_value = judge(get_a(W,data),data[0:5000,-1])
            #print('old_value:'+str(old_value))
            n = np.random.randint(0,9)
            W[n] = np.random.rand()
            new_value = judge(get_a(W,data),data[0:5000,-1])
            print('new_value:'+str(new_value))
            delta = new_value - old_value
            if delta > 0:
                W = W
            else:
                p = np.math.exp(delta/t)
                if p > np.random.rand():
                    W = W
        t = t*0.98       
    print(W)
    
'''