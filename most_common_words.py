#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 11:40
# @Author  : Aries
# @Site    : 
# @File    : most_common_words.py
# @Software: PyCharm
import re
import sys
from collections import Counter
try:
    number=int(sys.argv[1])
except:
    print("false usage: please your number of the most common")
    sys.exit()
counter=Counter(word.lower() for line in sys.stdin for word in line.strip().split() if re.search("[a-zA-Z]+",word))
for word,count in counter.most_common(number):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
