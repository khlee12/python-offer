#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 14:39:28 2018

@author: khlee

[面试题5]
逆向打印链表
"""

class linkedNode:
    value = -1
    nextNode = None
    
    def __init__(self, value, nextNode):
        self.value = value
        self.nextNode = nextNode
        

def printReverse(linkedList):
    stack = []
    while(linkedList):
        stack.append(linkedList.value)
        linkedList = linkedList.nextNode
        
    while(stack):
        print(stack.pop())
        
def printReverse2(linkedList):
    if (linkedList is None):
        return
    if (linkedList.nextNode is not None):
        printReverse2(linkedList.nextNode)
    print(linkedList.value)
        
'''
测试集
1）多个节点
node1 -> node2 -> node3 -> node4 -> node5
2）一个节点
node5
3）空
'''        
node5 = linkedNode(5, None)
node4 = linkedNode(4, node5)
node3 = linkedNode(3, node4)
node2 = linkedNode(2, node3)
node1 = linkedNode(1, node2)

printReverse(node1)
printReverse2(node1)
print('----')
printReverse(node5)
printReverse2(node5)
print('----')
nodenull = None
printReverse(nodenull)
printReverse2(nodenull)