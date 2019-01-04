#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 16:25
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo10.py
# @Software: PyCharm

# analyse the dataSet of the charpterDemo10
import math
from collections import Counter
import matplotlib.pyplot as plt
def bucketize(point,buck_size):
    return buck_size*(math.floor(point/buck_size))
def make_histogram(points,buck_size):
    return Counter(bucketize(point,buck_size) for point in points)
def plot_histogram(points,buck_size,title=" "):
    count=dict(make_histogram(points,buck_size))
    print(count)
    plt.bar([key for key in count.keys()],count.values(),width=buck_size)
    plt.title(title)
    plt.show()
    return
if __name__ == '__main__':
    # import random
    from numpy import random
    uniform=[200*random.random()-100 for i in range(10000)]
    normal=[57*random.randn() for i in range(10000)]
    plot_histogram(uniform,10,"average distribution")
    plot_histogram(normal,10,"rann_distribution")



