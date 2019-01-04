#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 10:13
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo01.py
# @Software: PyCharm
# nums=[1,2,3,4,5,6]
# g=lambda x:x+1
# nums=[g(num) for num in nums]
# print(nums)

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
grades=[83,95,91,87,70,0,85,82,100,67,73,77,0]# 10 divided
decile=lambda x:x//10*10
histogram=[decile(grade) for grade in grades]
print(histogram)
# learning searborn is the senior matplotlib
count_num=Counter(histogram)
print(count_num)
plt.bar([x-4 for x in count_num.keys()],count_num.values(),6)#plt.plot(),plt.ba(),plt.hist(),plt.scatter()
plt.show()