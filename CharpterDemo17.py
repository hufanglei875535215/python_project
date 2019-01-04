#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 15:29
# @Author  : Aries
# @Site    : 
# @File    : CharpterDemo17.py
# @Software: PyCharm
import random
from collections import Counter
from collections import defaultdict
import math
def entropy(class_probabilities):
    return sum(-p*math.log(p) for p in class_probabilities)
def class_probabilities(labels):
    nums=[]
    count=Counter(labels)
    for key in count.keys():
        nums.append(count[key]/len(labels))
    return nums
def data_entropy(labeled_data):
    labels=[label for training_set,label in labeled_data]
    class_pro=class_probabilities(labels)
    return entropy(class_pro)

def partition_entropy(subsets):
    total_count=sum(len(subset) for subset in subsets) ## subsets:[[[]],[[]],[[]]] subset:[[]]
    return sum(data_entropy(subset)*len(subset)/total_count for subset in subsets)

# first divide the data into many parts
def partition_by(inputs,attribution):#[{},{}]
    groups=defaultdict(list)
    for input in inputs:
        key=input[0][attribution]#2d by the type of the data
        groups[key].append(input)
    return groups
def partition_by_attribution(inputs,attribution):
    groups=partition_by(inputs,attribution)
    # total_partition_entropy=0
    # subsets=[]
    # for key in groups.keys():
    #     subsets.append(groups[key])
    # for key in groups.keys():
    #     total_partition_entropy+=partition_entropy(groups[key])
    # return total_partition_entropy
    #defaultdict的厉害之处就是可以将所有的values组合成一个列表，牛逼的功能
    return partition_entropy(groups.values())
###########################################################################################################
# 定义一个分类函数或者是回归函数用来表示相应的决策过程
#之前的代码都只是进行一个最优特征的分裂
#首先构建一棵决策树，返回树的头结点tree结点,二分类的情况
def build_tree_id3(inputs,split_candidates=None):#[[],[]]
    if(split_candidates is None):
        split_candidates=inputs[0][0].keys()
    nums_inputs=len(inputs)
    nums_trues=len([label for data,label in inputs if label==True])
    nums_false=len([label for data,label in inputs if label==False])
    if(nums_trues==0):return False
    if(nums_false==0):return True
    if(not split_candidates):
        return nums_trues>=nums_false
    # best_attribution=min(split_candidates,key=partial(partition_by_attribution,inputs))
    #首先得到best_attribution
    best_attribution=""
    max_CrossEntropy=-float("inf")
    for candition in split_candidates:
        if(partition_by_attribution(inputs,candition)>max_CrossEntropy):
            max_CrossEntropy=partition_by_attribution(inputs,candition)
            best_attribution=candition
    new_candidates=[Candidate for Candidate in split_candidates if Candidate!=best_attribution]
    subsets=partition_by(inputs,best_attribution)
    subtrees={attribute_value:build_tree_id3(subset,new_candidates)for attribute_value,subset in subsets.items()}
    subtrees[None]=nums_trues>nums_false
    return (best_attribution,subtrees)
################################################################################################################
def classify(tree,input):#{：，：，：，:}输入的单个样本的数据
    #也是要递归的调用
    if tree in [True,False]:
        return tree
    attribute,subtree_dict=build_tree_id3(input)
    subtree_key=input.get(attribute)
    if subtree_key not in subtree_dict.keys():
        subtree_key=None #所以决策树可以处理缺失值的算法，原因就是当前节点的缺失不会影响下一个结点的判断
    subtree=subtree_dict[subtree_key]
    return classify(subtree,input)




