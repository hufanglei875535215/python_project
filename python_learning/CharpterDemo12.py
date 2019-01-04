#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 10:36
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo12.py
# @Software: PyCharm

from collections import Counter
from collections import defaultdict
import CharpterDemo02
import numpy as np
import random
import matplotlib.pyplot as plt
from CharpterDemo02 import distance
def raw_majority_vote(labels):
    count=Counter(labels)
    return count.most_common(1)[0]#返回出现次数最多的一个 输出出现的次数以及相应的标签
#knn简单算法
def knnClassification(k,labeled_point,new_point):
    by_distance=sorted(labeled_point,key=lambda point:distance(point,new_point))
    k_nearst_label=[label for label in by_distance[:k]]#选出k个距离最近的样本数据
    return raw_majority_vote(k_nearst_label)

def random_point(dim):
    return [random.random() for  i in range(dim)]
def random_distances(dim,num_paris):
    return [distance(random_point(dim),random_point(dim))for i in range(num_paris)]
def random_point_numpy(dim):
    return np.random.random(dim)
# 计算出每个维度随机样本点的平均距离
#假设有10000个随机样本点
dimensions=[i for i in range(1,101)]
mean_distance=[]
min_distance=[]
for dim in range(1,101):
    mean_distance.append(np.mean(random_distances(dim,10000)))
    min_distance.append(np.min(random_distances(dim,10000)))
plt.plot(mean_distance)
plt.plot(min_distance)
plt.show()
# if __name__ == '__main__':
