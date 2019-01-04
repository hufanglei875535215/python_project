#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 21:38
# @Author  : Aries
# @Site    :this is the introduction part of the book of data science
# @File    : Introduction.py
# @Software: PyCharm
users=[{"id":0,"name":"Hero"},
{"id":1,"name":"Hero1"},
{"id":2,"name":"Hero2"},
{"id":3,"name":"Hero3"},
{"id":4,"name":"Hero4"},
{"id":5,"name":"Hero5"},
{"id":6,"name":"Hero6"},
{"id":7,"name":"Hero7"},
{"id":8,"name":"Hero8"},
{"id":9,"name":"Hero9"}
      ]
friends=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]
for user in users:
    user["friends"]=[]
for i,j in friends:
    users[i]["friends"].append(users[j]["id"])
    users[j]["friends"].append(users[i]["id"])
# print(users)
def number_of_friend(user):
    return len(user["friends"])
total_connection=sum(number_of_friend(user) for user in users)
# print(total_connection/10)
#
sorted_user=sorted(users,key=lambda x:len(x["friends"]),reverse=True)
print(sorted_user)
print(sorted_user[0]["name"])
# 统计出盆友的盆友
def friend_of_friend(user):
    friends=user["friends"]
    fof=[]
    for id  in friends:
        for j in users[id]["friends"]:
            fof.append(j)
    return fof
print(friend_of_friend(users[0]))

#统计出两个人之间共同的盆友
def common_friends(user1,user2):
    user1_friend=set(user1["friends"])
    user2_friend=set(user2["friends"])
    return list(user1_friend&user2_friend)
# print(common_friends(users[2],users[1]))
from collections import defaultdict
def friends_of_friends_id(user):
    friends=user["friends"]
    my_dict=defaultdict()
    for friend in friends:
        my_dict[users[friend]["id"]]=len((common_friends(user,users[friend])))
    return dict(my_dict)
print(friends_of_friends_id(users[0]))
