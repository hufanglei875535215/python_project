#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 11:08
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo03.py
# @Software: PyCharm
#分位数的概念情况
#分位数是中位数一种延生
import CharpterDemo02
import math
from collections import Counter
from CharpterDemo02 import squared_distance,sum_of_square,dot
def quantile(x,p):
    p_index=int(p*len(x))
    return sorted(x)[p_index]
#计算分位数之差
def quantile_range(x):
    return quantile(x,0.75)-quantile(x,0.25)
#计算反差
def mean(x):
    return sum(x)/len(x)
def de_mean(x):
    return [x_i-mean(x) for x_i in  x]
def variance(x):
    return sum_of_square(de_mean(x))/(len(x)-1)
def standard_deviation(x):
    return math.sqrt(variance(x))
def covariance(x,y):
    x_mean=de_mean(x)
    y_mean=de_mean(y)
    return dot(x_mean,y_mean)/(len(x)-1)
def correlation(x,y):
    return correlation(x,y)/(standard_deviation(x)*standard_deviation(y))
#验证中心极限定理
import random
def bernoulli_trail(p):
    return 1 if random.random()<p else 0
def binomial(n,p):
    return sum(bernoulli_trail(p) for i in range(n))
import matplotlib.pyplot as plt
def noraml_cdf(x,mu,sigma):
    return math.erf((x-mu)/sigma/math.sqrt(2))/2+1
def make_hist(p,n,num_points):
    data=[binomial(n,p) for i in range(num_points)]
    historgram=Counter(data)
    plt.bar([x-0.4 for x in historgram.keys()],[v/num_points for v in historgram.values()],0.8,color="0.75")
    mu=p*n
    sigmoid=math.sqrt(n*p*(1-p))
    xs=range(min(data),max(data)+1)
    ys=[noraml_cdf(x+0.5,mu,sigmoid)-noraml_cdf(x-0.5,mu,sigmoid) for x in xs]
    plt.plot(xs,ys)
    plt.show()
make_hist(0.76,100,10000)
