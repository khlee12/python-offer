#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:02:38 2018

@author: khlee

[面试题7]
用两个栈实现队列
"""
class Queue:
    def __init__(self):
        # for append
        self.stack1 = []
        # for delete
        self.stack2 = []
        
    def appendTail(self, value):
        self.stack1.append(value)
    
    def deleteHead(self):
        if len(self.stack2) > 0:
            self.stack2.pop()
            return True
        else:
            if len(self.stack1) > 0:
                while len(self.stack1)>0:
                    value = self.stack1.pop()
                    self.stack2.append(value)
                self.stack2.pop()
                return True
        return False
                
    def printQueue(self):
        if len(self.stack2) > 0:
            i = len(self.stack2)-1
            while i>=0:
                print(self.stack2[i])
                i -= 1
        if len(self.stack1) > 0:
            for i in range(len(self.stack1)):
                print(self.stack1[i])
                
                
# 测试集
queue = Queue()
#在空队列删除元素
queue.deleteHead()
#正常往队列加入与删除
queue.appendTail(1)
queue.appendTail(5)
queue.appendTail(3)
queue.deleteHead()
queue.appendTail(4)
queue.deleteHead()
queue.printQueue()
#连续删除元素直到队列为空
while 1:
    result = queue.deleteHead()
    if result == False:
        break
queue.printQueue()