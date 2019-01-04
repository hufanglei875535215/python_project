#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 11:28
# @Author  : Aries
# @Site    : 
# @File    : egrep.py
# @Software: PyCharm
import re
import sys
regrex=sys.argv[1]
for line in sys.stdin:
    if(re.search(regrex,line)):
        sys.stdout.write(line)