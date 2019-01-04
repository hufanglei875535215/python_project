#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 21:57
# @Author  : Aries
# @Site    : 
# @File    : New_Class_Learning.py
# @Software: PyCharm
# class Parent:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(self.name)
# class Son(Parent):
#     def showSon(self):
#         print("the current name is {0}".format(self.name))
# if __name__ == '__main__':
#     son = Son("weiminghu")
#     son.showSon()

class Person:
    def __init__(self,name,job=None,pay=0):
        self.name=name
        self.job=job
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay=self.pay*(1+percent)
    def __str__(self):
        return "[Person: %s,%s]"%(self.name,self.pay)
class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self,name,"manager",pay)
    def giveRaise(self,percent,bonus=0.1):
        Person.giveRaise(self,percent+bonus)
class Department:
    def __init__(self,*args):
        self.members=list(args)
    def addMember(self,person):
        self.members.append(person)
    def giveRaise(self,percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAllMembers(self):
        for person in self.members:
            print(person)
if __name__ == '__main__':
    bob = Person("weiminghum")
    sue = Person("lisijia")
    tom = Manager("qingtao",100)
    department=Department(bob,sue)
    department.addMember(tom)
    department.showAllMembers()
