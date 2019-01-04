#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 16:56
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo11.py
# @Software: PyCharm

#making the circle
import numpy as np
def split_data(data,pro,random_seed=33):
    results=[],[]
    for row in data:
        results[0 if np.random.random(random_seed)>pro else 1].append(row)
    return results
def train_test_split(X,y,test_size,random_seed):
    X_train=split_data(X,test_size,random_seed)[0]
    X_test=split_data(X,test_size,random_seed)[1]
    y_train,y_test=split_data(y,test_size,random_seed)[0],split_data(y,test_size,random_seed)[1]
    return X_train,X_test,y_train,y_test
def accuracy(tp,fp,fn,tn):
    correct=tp+tn
    return correct/(tp+fp+fn+tn)
def precision(tp,fp,fn,tn):
    # positive=tp
    return tp/(tp+fp)
def recall(tp,fp,fn,tn):
    return tp/(tp+fp)
def f1_score(tp,fp,fn,tn):
    p=precision(tp,fp,fn,tn)
    r=recall(tp,fp,fn,tn)
    return 2*p*r/(p+r)


