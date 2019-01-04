#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/24 11:53
# @Author  : Aries
# @Site    : 
# @File    : GroupByDemo02.py
# @Software: PyCharm
#基于分组的apply的应用
#首先是分位数
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
frame=DataFrame({"data1":np.random.randn(1000),"data2":np.random.randn(1000)})
factor=pd.cut(frame.data1,4)#由cut得到的对象可以用于直接groupby到其他相应的df中
print(factor)
groupby9=frame.data2.groupby(factor)
# print(groupby.mean())
def get_stats(group):
    return {"max":group.max(),"min":group.min(),"count":group.count(),"mean":group.mean()}
print(groupby9.apply(get_stats))
print(groupby9.apply(get_stats).unstack())

#所以使用agg默认使用的还是apply方法
def agg(group):
    return {"max":group.max(),"min":group.min(),"count":group.count(),"mean":group.mean(),"total":[group.max(),group.min()]}
print(groupby9.apply(agg).unstack())
#等价于
# print(groupby9.agg([]||{})
print(groupby9.agg(["max","min","count"]))
print(groupby9.agg({"total":["max","min","count"]}))

#用于分组填充的groupby的使用 +apply
def fill_na_group(group):
    group.fillna(group.mean())
data=Series(np.random.randn(8),index=['o','N',"V",'F',"N1","C","I","K"])
data[['o','N','C','I']]=np.nan
print(data.groupby(["East"]*4+['west']*4).apply(fill_na_group)) #可以填充相应的缺失值
print("*888888888888888888888888888888888888888888")
#分组计算加权平均
df=DataFrame({"category":['a','a','a','a','b','b','b','b'],'data':np.random.randn(8),'weights':np.random.randn(8)})
print(df)
groupby10=df.groupby("category")
get_wavg=lambda g:np.average(g["data"],weights=g["weights"]) #对应的权重
final_data=groupby10.apply(get_wavg)
print(final_data)