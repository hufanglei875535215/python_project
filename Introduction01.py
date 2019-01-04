#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 22:29
# @Author  : Aries
# @Site    : 
# @File    : Introduction01.py
# @Software: PyCharm
salaries_and_tenures=[
    (83000,8.7),(88000,8.1),(48000,0.7),(76000,6),(69000,6.5),(76000,7.5),(60000,2.5),(83000,10),(48000,1.9),(63000,4.2)
    ]
def true_bucket(tenture):
    if tenture<2:
        return "less than 2"
    elif tenture<5:
        return "between 2 and 5"
    else:
        return "bigger than 5"
from collections import defaultdict
salary_and_tenture_per=defaultdict(list)
for salary,tenture in salaries_and_tenures:
    salary_and_tenture_per[true_bucket(tenture)].append(salary)
for item in salary_and_tenture_per.items():
    print(item[0])
    print(sum(item[1])/len(item[1]))
