#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:37:25 2018

@author: khlee

[面试题2]
实现Singleton模式
设计一个类，我们只能生成该类的一个实例
场景：单线程，多线程
想法：我们只是在实例还没有被创建之前需要加锁，以保证只有一个线程创建出实例
credit to: https://github.com/JushuangQiao/Python-Offer/tree/master/second/second
* check other methods such as __new__, __init__
"""

class Singleton:
    
    def __init__(self, val):
        self.val = val
        
single = Singleton(2)


a = single
b = single
print (a.val, b.val)
print (a is b)
a.val = 233
print (a.val,b.val) 
    