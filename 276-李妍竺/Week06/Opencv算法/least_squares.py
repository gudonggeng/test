import pandas as pd
import numpy as np
#('train_data.csv',sep='\s*,\s*',engine='python') #sep：分隔符，默认为， engine：所用引擎
train = pd.read_csv('train_data.csv')
print(train)

X = train['X'].values
Y = train['Y'].values

print(X)

n = len(X)
# 计算累加
s1 = np.sum(X * Y)
s2 = np.sum(X)
s3 = np.sum(Y)
s4 = np.sum(X * X)
print(s1)
#计算斜率和截距
k = (n * s1-s2 * s3)/(s4 * n-s2 * s2)
b = (s3 - k * s2)/n

print('Coeff:',k)
print('Intercept',b)
'''
#初始化赋值
s1 = 0
s2 = 0
s3 = 0
s4 = 0
n = 5   #根据数量改变

#循环累加
for i in range(n):
    s1 = s1 + X[i]*Y[i]     #X*Y，求和
    s2 = s2 + X[i]          #X的和
    s3 = s3 + Y[i]          #Y的和
    s4 = s4 + X[i]*X[i]     #X**2，求和
print(s1)
#计算斜率和截距
k = (s2*s3-n*s1)/(s2*s2-s4*n)
b = (s3 - k*s2)/n
print("Coeff: {} Intercept: {}".format(k, b))  #format:与{}配套使用


'''