#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 11:38
# @Author  : Aries
# @Site    : 
# @File    : String_Pandas.py
# @Software: PyCharm
#传统的字符串函数，不再这里过多的介绍了
import re
import numpy as np
from pandas import Series,DataFrame
text="fool bar \t baz \t qux"
names=re.split('\t',text)
print(names)

emails="Dave d.ave@google.com Steve steve@gmail.com"
pattern=re.compile(r"[a-z0-9_.%+-]+@[a-z0-9.-]+\.[a-z]{2,4}")
print(pattern.findall(emails))
data={"Dave":"dave@google.com",'steve':'stece@gmail.com','Rob':"rob@gmail.com","Wes":np.nan}
ss=Series(data)
print(ss.isnull())

print(ss.str.contains("com"))
print(ss.str.findall(pattern))#飞快的统计出所有匹配的字段出来了  nice相当nice，处理完数据之后可以将数据上传至hive等，但是现在是struct类型的数据;