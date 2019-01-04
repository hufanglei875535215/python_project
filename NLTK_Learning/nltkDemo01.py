#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 14:53
# @Author  : Aries
# @Site    : 
# @File    : nltkDemo01.py
# @Software: PyCharm
from nltk.book import *
from nltk.corpus import gutenberg
import nltk
from nltk.corpus import stopwords
# for fileid in gutenberg.fileids():
#     num_char=len(gutenberg.raw(fileid))
#     num_word=len(gutenberg.words(fileid))
#     # num_sents=len(gutenberg.sents(fileid))
#     num_vocab=len(set([w.lower() for w in gutenberg.words(fileid)]))
#     # print(int(num_char/num_word),int(num_word/num_sents),num_vocab)
#     print(num_char/num_word)
# if __name__ == '__main__':
#     古腾堡语料库的使用

#词典资源
def unusual_word(text):
    text_vocab=set(w.lower() for w in text if w.isalpha())
    all_words=set(w.lower() for w in nltk.corpus.words.words())
    return text_vocab.difference(all_words)
def content_fraction(text):
    stopwords=nltk.corpus.stopwords.words("english")
    content=[w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)
# 处理语义的包，包括同义词，下位词，反义词等
from nltk.corpus import wordnet as wn
import re


# if __name__ == '__main__':
    # print(unusual_word(gutenberg.words()))
    # print(content_fraction(nltk.corpus.reuters.words()))
    # print(wn.synsets("motorcar"))
    # print(wn.synset("car.n.01").lemma_names)
#     wordlist=[w for w in nltk.corpus.words.words("en") if w.islower()]
#     word_end_with_ed=[w for w in wordlist if re.search("ed$",w)]
#     print(word_end_with_ed[:10])
#     word_has_eight_num=[w for w in wordlist if re.search(r"^..j..t..$",w)]
#     print(word_has_eight_num)
#     words=[w for w in wordlist if re.search("^[ghi][mno][jlk][def]$",w)]
#     print(words)
# #   使用
#     chat_words=sorted(set(w for w in nltk.corpus.nps_chat.words()))
#     new_words=[w for w in chat_words if re.search("^m+i+n+e+$",w)]
#     print(new_words)
#     pattern="9876search@"
# # 使用正则表达式进行相应的题干的提取，什么是题干，提干就是指词的主干部分，不如ing，ed等都是统一个词;
#     ans=re.findall(r"^.*(ing|ed|es|ly|s|ment|ies|ious|ive|)","processing")
#     print(ans)
#     nums=[]
#     nums1=[[],[],[]]
#     nums1[1].append("hello world")
#     print(nums1)
#     词性标注器，用来标注词的词性，形容词，动词，名词等
#     text=nltk.word_tokenize("And now for something completely difference")
#     print(nltk.pos_tag(text))
#     import nltk
#     from nltk.corpus import brown
#     def process(sentence):
#             for(w1,t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
#                 if(t1.startswith("V") and t2 =="TO" and t3.startswith("V")):
#                     print(w1,w2,w3)
#     for tagged_sentence in brown.tagged_sents():
#         process(tagged_sentence)

# 文本分析之模型训练
# ###########################################################################
# 定义一个特征提取器用来提取相应的特征，这里简单定义了一个函数                  #
#
#############################################################################

# def gender_feature(word):
#     return {"laster_letter":word[-1],"length":len(word),"end_word":word.endswith("s")}
# # from nltk.corpus import names
# # import random
# # all_names=([(name,"male")for name in names.words("male.txt")]+[(name,"female") for name in names.words("female.txt")])
# # random.shuffle(all_names)
# # print(all_names[:10])
# # featuresets=[(gender_feature(word),g) for (word,g)in all_names]
# # # print(featuresets[:100])
# # print(featuresets[:10])
# # train_sets,test_sets=featuresets[500:],featuresets[:500]
# # classifier=nltk.NaiveBayesClassifier.train(train_sets)
# # print(classifier.classify(gender_feature("hufanglei")))
# # print(classifier.classify(gender_feature("scarlet")))
# # print(nltk.classify.accuracy(classifier,test_sets))
# # print(classifier.show_most_informative_features(5))
# ###########################################################################
# 定义一个特征提取器用来提取相应的特征，这里简单定义了一个函数                  #
#使用较为复杂的特征，使其适当的过拟合
#############################################################################
import string
def gender_features(name):
    features={}
    features["firstletter"]=name[0].lower()
    features["lastletter"]=name[-1].lower()
    for letter in string.ascii_lowercase:
        features["count(%s)"%letter]=name.lower().count(letter)
        features["has({0})".format(letter)]=letter in name.lower()
    return features
# print(gender_features("weiminghu"))
# if __name__ == '__main__':
#     names=[(name,"male") for name in nltk.corpus.names.words("male.txt")]+[(name,"female")for name in nltk.corpus.names.words("female.txt")]
#     data=[(gender_features(name),label) for name,label in names]
#     print(len(data))
#     training_data=data[1500:]
#     testing_data=data[:500]
#     classifier=nltk.NaiveBayesClassifier.train(training_data)
#     print(nltk.classify.accuracy(classifier,testing_data))
#     validation_data=names[500:1000]
#     errors=[]
#     for name,tag in validation_data:
#         predict=classifier.classify(gender_features(name))
#         if(predict!=tag):
#             errors.append((name,tag,predict))
#     errors.sort()
#     for name,tag, predict in errors[:10]:
#         print("name=%-30s "%name+"tag=%-8s"%tag+"predict=%-8s"%predict)

# ###########################################################################
# 文档分类模型的建立                                                         #
#
#############################################################################
#建立文档 这里使用movie文档中的内容，对文档进行正向和负向的评价
from nltk.corpus import movie_reviews
import random
document=[(list(movie_reviews.words(fileid)),tag) for tag in movie_reviews.categories() for fileid in movie_reviews.fileids(tag)]
random.shuffle(document)
# print(document[:10])
#构建特征，如何构建呢？最简单的构建方式是改词是否在words库中出现过，所以就是one-hot模型
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features=list(all_words.keys())[:2000]
def get_feature_doc(document):
    words=set(document)
    features={}
    for word in word_features:
        features["contains{0}".format(word)]=word in words
    return features
# if __name__ == '__main__':
#     # print(get_feature_doc(movie_reviews.words("pos/cv957_8737.txt")))
#     #构建训练样本
#     total_data=[(get_feature_doc(doc),label) for doc,label in document]
#     train_set=total_data[100:]
#     test_set=total_data[:100]
#     classifier=nltk.NaiveBayesClassifier.train(train_set)
#     print(nltk.classify.accuracy(classifier,test_set))
#     print(classifier.most_informative_features(10))

# ###########################################################################
# 词性标注分类模型的建立                                                         #
#分类模型中的一种，构建词性分类器，nltk中的词性分类器
#############################################################################
from nltk.corpus import brown
suffix_dict=nltk.FreqDist()
for word in brown.words():
    word=word.lower()
    suffix_dict[word[-1:]]+=1
    suffix_dict[word[-2:]]+=1
    suffix_dict[word[-3:]]+=1
common_suffixes=list(suffix_dict.keys())[:100]
# print(common_suffixes)
def pos_features(word):
    feature={}
    for key in common_suffixes:
        feature["contains%s"%key]=word.lower().endswith(key)#通过频繁出现的词构建词向量
    return feature
# if __name__ == '__main__':
#     total_data=[(pos_features(word),target) for word,target in brown.tagged_words(categories="news")]
#     print(total_data[0])
#     size=int(len(total_data)*0.1)
#     train_data,test_data=total_data[size:],total_data[:size]
#     classifier=nltk.DecisionTreeClassifier.train(train_data)
#     print(nltk.classify.accuracy(classifier,test_data))
#     print(classifier.classify(pos_features("cats")))
#     print(classifier.pseudocode(depth=4))

# ###########################################################################
# 建立分类器用来
# 探索上下文的语境
#依赖上下文的特征提取器来定义一个词性标记分类器
#############################################################################
#也就是在考虑词性的同时将该词的前一个单词的词也考虑进去
from nltk.corpus import brown
def pos_feature(sentence,i):
    features={
        "suffix(1)":sentence[i][-1:],
        "suffix(2)":sentence[i][-2:],
        "suffix(3)":sentence[i][-3:]
    }
    if(i==0):
        features["pre-word"]="<start>"
    else:
        features["pre-word"]=sentence[i-1]
    return features
# if __name__ == '__main__':
#     featuresets=[]
#     for tagged_sent in brown.tagged_sents(categories="news"):
#         untagged_sent = nltk.tag.untag(tagged_sent)
#         #首先去除tag
#         for i,(word,tag) in enumerate(tagged_sent):
#             featuresets.append((pos_feature(untagged_sent,i),tag))
#     # print(featuresets[:5])
#     size=int(len(featuresets)*0.1)
#     train_set=featuresets[size:]
#     test_set=featuresets[:size]
#     classifier=nltk.classify.NaiveBayesClassifier.train(train_set)
#     print(nltk.classify.accuracy(classifier,test_set))

# ###########################################################################
# 建立分类器用来
# 探索上下文的语境
# 依赖上下文中的词性将词性也考虑作为训练的一维特征考虑进去
#############################################################################
def pos_feature_tag(sentence,i,history_tag):
    features={
        "suffix(1)":sentence[i][-1:],
        "suffix(2)":sentence[i][-2:],
        "suffix(3)":sentence[i][-3:]
    }
    if i==0:
        features["pre-word"]="<start>"
        features["pre-tag"]="<start>"
    else:
        features["pre-word"]=sentence[i-1]
        features["pre-tag"]=history_tag[i-1]
    return features

class ConsecutivePosTagger(nltk.TaggerI):
    def __init__(self,train_sents):#[["","","",""],["","","",""]]
        train_sets=[]
        for tagged_sent in train_sents:
            untagged_sent=nltk.untag(tagged_sent)
            history=[]
            for i,(word,tag) in enumerate(tagged_sent):
                train_sets.append((pos_feature_tag(untagged_sent,i,history),tag))
                history.append(tag)
        self.classifier=nltk.classify.NaiveBayesClassifier.train(train_sets)
    def tag(self,sentence):
        history=[]
        feature_set=[]
        taggers=[]
        for i,word in enumerate(sentence):
            feature_set=pos_feature_tag(sentence,i,history)
            tag=self.classifier.classify(feature_set)
            history.append(tag)
            taggers.append(tag)
        return zip(sentence,taggers)


if __name__ == '__main__':
    sentences=brown.tagged_sents(categories="news")
    # tagger=ConsecutivePosTagger(sentences)
    # print([(word,tag)for word,tag in tagger.tag(["i","am","a","gir","who","are","so","beautiful"])])
    size=int(len(sentences)*0.1)
    train_set,test_set=sentences[size:],sentences[:size]
    tagger=ConsecutivePosTagger(train_set)
    print(tagger.evaluate(test_set))






