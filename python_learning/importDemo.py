#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 18:29
# @Author  : Aries
# @Site    : 
# @File    : importDemo.py
# @Software: PyCharm


#python_learning.importDemo
print(__name__) #导包的时候输出的是包名，但是main函数执行的时候输出的是 __main__
def self_fun(test,*args):
    ans=args[0]
    for arg in args[1:]:
        if(test(arg,ans)):
            ans=arg
    return ans
def maxNum(x,y):
    return x>y
def minNum(x,y):
    return x<y
#这种写法在使用每次第一次导入的时候会执行输出语句，所以要把相应的测试代码放到main目录下
if __name__ == '__main__':
    print(self_fun(maxNum, (1, 2, 3, 4, 5)))# 默认可变参数是多个变量，不能是元祖或是列表的形式进行参数传递;
    print(self_fun(maxNum,1,2,3,4,5))
    from python_learning.CharpterDemo13 import NaiveBayesClassifier

