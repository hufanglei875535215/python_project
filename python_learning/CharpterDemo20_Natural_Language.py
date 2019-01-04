#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/30 14:12
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo20_Natural_Language.py
# @Software: PyCharm
import matplotlib.pyplot as plt
from collections import defaultdict
import random
data=[("big_data",100,15),("Hadoop",95,25),("python",75,50),
      ("R",50,40),("machine learning",80,20),("statistics",20,60),("data science",60,70),("analytics",90,3),("team player",85,85),("dynamic",2,90),("synerrgies",70,0)]
def text_size(total):
    return 8+total/200*20

#二元模型
line=". my name is hufanglei this is my first time to learning nature language process what i am know is just machine learning process ."
document=line.strip().split()
bigrams=zip(document,document[1:])
transitions=defaultdict(list)
for prev,current in bigrams:
    transitions[prev].append(current)
def generate_using_bigrams():
    current="."
    result=[]
    while True:
        next_word_candidate=transitions[current]
        next_word=random.choice(next_word_candidate)
        result.append(next_word)
        current=next_word
        if current==".":
            return " ".join(result)

#三元模型
biggrams3=zip(document,document[1:],document[2:])
trigram_transitions=defaultdict(list)
starts=[]
for pre,current,next in trigram_transitions:
    if pre==".":
        starts.append(current)
    trigram_transitions[(pre,current)].append(next)
    #defaultdict的功能可以使用元组作为键
if __name__ == '__main__':
    new_line=generate_using_bigrams()
    print(new_line)



# if __name__ == '__main__':
    # data = [("big_data", 100, 15), ("Hadoop", 95, 25), ("python", 75, 50),
    #         ("R", 50, 40), ("machine learning", 80, 20), ("statistics", 20, 60), ("data science", 60, 70),
    #         ("analytics", 90, 3), ("team player", 85, 85), ("dynamic", 2, 90), ("synerrgies", 70, 0)]
    # for word,job_popu,resume_popu in data:
    #     plt.text(job_popu,resume_popu,word,ha="center",va="center",size=text_size(job_popu+resume_popu))
    # plt.xlabel("popularity on job popular")
    # plt.ylabel("popularity on resume popular ")
    # plt.axis([0,100,0,100])
    # plt.xticks([])
    # plt.yticks([])
    # plt.show()
