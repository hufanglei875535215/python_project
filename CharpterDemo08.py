#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 10:45
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo08.py
# @Software: PyCharm
# this part is mainly about the Gradient part
def sum_of_square(v):
    return sum(value**2 for value in v)
def difference_quotient(f,x,h):
    return (f(x+h)-f(x))/h
#partition_ Gradient

def partition_difference_quotient(f,x,i,h):
    #f(x1,x2,x3,x4+h,x5...)
    new_vector=[value+(h if i==j else 0)for j,value in enumerate(x)]
    return (f(new_vector)-f(x))/h
#step
def step(v,direction,step_size):
    return [value+direction_value*step_size for value,direction_value in zip(v,direction)]
def sum_of_square_gradient(v):
    return [2*value for value in v ]
def distance(v1,v2):
    min_vector=[value1-value2 for value1,value2 in zip(v1,v2)]
    return sum(value*value for value in min_vector)
def safe(f):
    def safe_f(*args,**Kwargs):
        try:
            return f(*args,**Kwargs)
        except:
            return float("inf")
    return safe_f
if __name__ == '__main__':
    import random
    tolance=0.000000000001
    vector=[random.randint(-10,10) for i in range(3)]
    step_size=-0.01
    while True:
        gradient=sum_of_square_gradient(vector)
        new_vector=step(vector,gradient,step_size)
        if(distance(new_vector,vector)<tolance):
            print(new_vector)
            break
        vector=new_vector



