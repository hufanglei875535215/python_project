#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 11:29
# @Author  : Aries
# @Site    : 
# @File    : line_count.py
# @Software: PyCharm
import sys
count=0
for line in sys.stdin:
    count+=1
print(count)

# import sys
# line=sys.stdin.readline()
# sys.stdout.write(line)