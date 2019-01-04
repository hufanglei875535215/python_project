#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 14:18
# @Author  : Aries
# @Site    : 
# @File    : nltkDemo02.py
# @Software: PyCharm
# import nltk
# from nltk.corpus import stopwords
# print(stopwords.words("english"))
# sentence="I always lie down to tell a lie"
# print(nltk.word_tokenize(sentence))
# import nltk
# my_grammer=nltk.CFG.fromstring("""
# S -> NP VP
# PP -> P NP
# NP -> Det N | Det N PP | 'I'
# VP -> V NP | VP PP
# Det -> 'an' | 'my'
# N -> "elephant" | "pajamas"
# V -> 'shot'
# P -> 'in'
# """)
# parser=nltk.ChartParser(my_grammer)
# sentence=nltk.word_tokenize("I shot an elephant in my pajamas")
# for tree in parser.parse(sentence):
#     print(tree)

