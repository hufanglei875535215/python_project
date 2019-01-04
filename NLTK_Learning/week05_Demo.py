#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 22:24
# @Author  : Aries
# @Site    : 
# @File    : week05_Demo.py
# @Software: PyCharm
#这里的内容是炼数成精中的第五周的内容，关于相应的中文分词;

##########
# 中文分词
# --基于字典，词库匹配
# --基于词频统计
# --基于知识理解
##########
# 基于字典匹配的方法，从字典中进行匹配
# ----正向最大匹配
# ----逆向最大匹配
# ----双向最大匹配
# ----设立切分标志法
# ----最佳匹配
###########

##########
#基于词频度的统计
#--基于N-gram模型
#--基于HMM模型
#--基于字标注的中文分词方法

#jieba分词的使用
#--分词
#--添加自定义词典
#--关键词提取
#--词性标注

#############
# 所有代码位于
# https://github.com/fxsjy/jieba
import jieba
import sys
import jieba
import jieba.analyse
from optparse import OptionParser #学习脚本的配置
#jieba.cut() param:string,cut_all.HMM
#jieba.cut_for_search() param,ter:string cut_all
ss="我是北京大学的学生，我的名字是胡方磊"
print([item for item in jieba.cut(ss)])
print([item for item in jieba.cut_for_search(ss,HMM=False)])

#同时jieba还支持相应的载入字典，也就是说载入自己定义的词语
#...
#结巴关键词的提取
#基于tf-idf算法的提取关键词
import jieba.analyse
key_words=jieba.analyse.extract_tags("我是北京大学的学生，我的名字是胡方磊")
# key_words=jieba.analyse.extract_tags(s//f.read())#或者是读取文件中的所有的参数
print(" ".join(key_words))
#基于TextRank的关键词的抽取
key_words=jieba.analyse.textrank("我是北京大学的学生，我的名字是胡方磊")
print(",".join(key_words))
#词性标注
import jieba.posseg  as pseg
words=pseg.cut("我是北京大学的学生，我的名字是胡方磊")
for word,tag in words:
    print("{0}:{1}".format(word,tag))
#并行分词;
#ChineseAnalyzer for Whoosh 搜索引擎

