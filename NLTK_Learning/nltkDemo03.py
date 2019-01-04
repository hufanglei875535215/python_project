#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 21:38
# @Author  : Aries
# @Site    : 
# @File    : nltkDemo03.py
# @Software: PyCharm

#题干提取中的内容，进行自然语言处理的文本处理阶段首先需要的就是
#文本标准化，提纲词提取，词型归并，然后分词，构建词向量等
import nltk
#可以使用正则化或者是传统的字符处理
# raw = """DENNIS: Listen, strange women lying in ponds distributing swords
#     is no basis for a system of government.  Supreme executive power derives from
#     a mandate from the masses, not from some farcical aquatic ceremony."""
# words=nltk.word_tokenize(raw)
# porter=nltk.PorterStemmer()
# lancaster=nltk.LancasterStemmer()
# print([porter.stem(t) for t in words])
# print([lancaster.stem(t) for t in words])
# """
# ['denni', ':', 'listen', ',', 'strang', 'women', 'lie', 'in', 'pond', 'distribut', 'sword', 'is', 'no', 'basi', 'for', 'a', 'system', 'of', 'govern', '.', 'suprem', 'execut', 'power', 'deriv', 'from', 'a', 'mandat', 'from', 'the', 'mass', ',', 'not', 'from', 'some', 'farcic', 'aquat', 'ceremoni', '.']
# ['den', ':', 'list', ',', 'strange', 'wom', 'lying', 'in', 'pond', 'distribut', 'sword', 'is', 'no', 'bas', 'for', 'a', 'system', 'of', 'govern', '.', 'suprem', 'execut', 'pow', 'der', 'from', 'a', 'mand', 'from', 'the', 'mass', ',', 'not', 'from', 'som', 'farc', 'aqu', 'ceremony', '.']
# """
#
# #词形归并 women变为了woman，复数变为了单数等;
# wnl=nltk.WordNetLemmatizer()
# print([wnl.lemmatize(t) for t in words])

##使用nltk.re_show()进行相应的正则表达式的检查
print(nltk.re_show("[A-Za-z]+","abcd123"))
print(nltk.re_show("[A-Z][a-z]*","asDd123B"))
print(nltk.re_show("p[aeiou]{,2}t","apaetioo2"))
print(nltk.re_show("\d+(\.\d+)","adf12.34"))
print(nltk.re_show("[^aeiou][aeiou][^aeiou]","papppipepip"))
