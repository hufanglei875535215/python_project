#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 17:26
# @Author  : Aries
# @Site    : 
# @File    : GroupByDemo.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
df=DataFrame({"key1":['a','a','b','b','a'],
              'key2':['one','two','one','two','one'],
              'data1':np.random.randn(5),
              "data2":np.random.randn(5)})
print(df)
grouped=df["data1"].groupby(df["key1"])
print(grouped.mean())# grouped.sum(), grouped.std(),group
# key1
# a    1.111794
# b    0.085202
# grouped2=df["data1"].groupby(df[["key1","key2"]])
# print(df[["key1","key2"]])
grouped2=df["data1"].groupby([df["key1"],df["key2"]])
print(grouped2.mean())
print(grouped2.mean().unstack())

#foramt
#array or Series. groupby(array or [array,array])

#THE DF FORMART IS  A BIT DIFFERENT
grouped3=df.groupby(["key1","key2"])
print(grouped3.mean())
print(grouped3.mean().unstack())

#using the show part
for name,group in df.groupby("key1"):
    print(name)
    print(group)

for (k1,k2),group in df.groupby(["key1","key2"]):
    print(k1,k2)
    print(group)
print("____________")
df_dtype=df.dtypes
grouped4=df.groupby(df_dtype,axis=1)

for name,group in grouped4:
    print(name)
    print(group)


print("下面是高级用法，面向多列的函数聚合应用")
def self_agg(arry):
    return arry.max()-arry.min()
grouped08=df.groupby("key1")
print(grouped08.agg(["mean","sum","std",self_agg]))

#或者使用map进行映射构建新的聚合函数,对不同的分组进行不同的运算
function_map={"data1":np.max,"data2":self_agg}
print(grouped08.agg(function_map))