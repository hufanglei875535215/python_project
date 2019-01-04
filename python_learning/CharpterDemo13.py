#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 11:34
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo13.py
# @Software: PyCharm
import re
from collections import defaultdict
from collections import Counter
import math
def tokensize(message):
    message=message.lower()
    all_words=re.findall(r"[a-z0-9]+",message)
    return set(all_words)
#统计出一个字典，字典中的健是字符串,值是列表

def count_word(training_set):#[feature,label]
    counts=defaultdict(list)
    for features,labels in training_set:
        for word in tokensize(features):
            counts[word][1 if labels else 0]+=1
    return counts
#计算出每一个词的概率
def word_probabilities(count,total_spams,total_non_spams,k=0.5):
    #return (w,p(w|spam),p(w|^spam))
    return [(w,(count[w][0]+k)/(total_spams+2*k),(count[w][1]+k)/(total_non_spams+2*k))for w in count.keys()]
def spam_propability(word_probs,message):
    #针对一个新的message,新的邮件，需要给邮件赋予新的概率
    words=tokensize(message)
    log_is_spam_pro=log_is_not_spam_pro=0.0
    for word,is_spam_pro,is_not_spam_pro in word_probs:
        if word in words:
            log_is_spam_pro+=math.log(is_spam_pro)
            log_is_not_spam_pro+=math.log(is_not_spam_pro)
        else:
            log_is_spam_pro+=math.log(1-is_spam_pro)
            log_is_not_spam_pro+=math.log(1-is_not_spam_pro)
    pro_if_spam=math.exp(log_is_spam_pro)
    pro_if_not_spam=math.exp(log_is_not_spam_pro)
    return pro_if_spam/(pro_if_spam+pro_if_not_spam)
class NaiveBayesClassifier:
    def __init__(self,k=0.5):
        self.k=k
        self.word_probs=[]
    def train(self,training_set):
        num_spams=len([is_spam for message,is_spam in training_set if is_spam])
        num_not_spam=len(training_set)-num_spams
        counts=count_word(training_set)
        self.word_probs=word_probabilities(counts,num_spams,num_not_spam,self.k)
    def classify(self,message):
        #带参数的变量也要在该函数的形参中 才能进行传递
        return spam_propability(self.word_probs,message)



