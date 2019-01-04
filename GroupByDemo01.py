#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 17:59
# @Author  : Aries
# @Site    : 
# @File    : GroupByDemo01.py
# @Software: PyCharm

#如果需要groupby的列没有重复值，此时如果需要相应的groupby,此时需要通过字典进行相应的作为聚合的对象
import pandas as pd
from pandas import DataFrame,Series
import numpy as np
people=DataFrame(np.random.randn(5,5),columns=['a','b','c','d','e'],index=['hufanglei','weiminghu','lisijia','scallte','huoxinxin'])
people.loc[2:3,["b","c"]]=np.nan
# print(people)
#希望通过列来进行聚合相应的表中的数据
mapping={"a":"one","b":"one","c":"two","d":"three","e":"one","f":"four"}
grouped5=people.groupby(mapping,axis=1)
print(grouped5.mean())

#使用函数进行相应的分组：
grouped6=people.groupby(len).mean()# people.groupby([len(0),len(1),len(2)...])
print(grouped6)

#可以手动添加一个函数进行定义
def weight(x):
    return 10
grouped7=people.groupby(weight).mean()
print(grouped7)
