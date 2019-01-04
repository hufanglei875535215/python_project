#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 10:30
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo02.py
# @Software: PyCharm
# vector calcualtion without numpy and pandas
#vector:
import math
def vector_add(x1,x2):
    return [value1+value2 for value1,value2 in zip(x1,x2)]
def vector_min(x1,x2):
    return [value1-value2 for value1,value2 in zip(x1,x2)]
def vector_sum(vectors):
    result=vectors[0]
    for vector in vectors[1:]:
        result=vector_add(result,vector)
    return result
def scalar_multiply(c,v):
    return [c*vi for vi in v]
def vector_mean(vectors):
    result=vector_sum(vectors)
    n=len(vectors)
    return scalar_multiply(1/n,result)
def dot(x1,x2):
    return sum([value1*value2 for value1,value2 in zip(x1,x2)])
def sum_of_square(v):
    return sum(value*value for value in v)
    #return dot(v,v)
def squared_distance(v1,v2):
    return sum_of_square(vector_min(v1,v2))
def distance(v1,v2):
    total=squared_distance(v1,v2)
    return math.sqrt(total)

#matric method
def shape(A):
    num_row=len(A)
    num_col=len(A[0]) if A else 0
    return num_row,num_col
def get_row(A):
    return shape(A)[0]
def get_col(A):
    return shape(A)[1]

def matric_add(A,B):
    return [vector_sum(v1,v2) for v1,v2 in zip(A,B)]
