#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 14:46:13 2018

@author: khlee

[面试题3]
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序
请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数
e.g.:
    1 2 8 9
    2 4 9 12
    4 7 10 13
    6 8 11 15
find 7
"""

def findNumber(matrix, search_num):
    if (object is None or search_num is None) :
        return -1
    if not isinstance(search_num, int):
        return -1
    if not isinstance(matrix, list):
        return -1
    
    rows = 0
    cols = len(matrix[0])-1
    # rows, cols = 0, len(matrix[0])-1
    
    rows_max = len(matrix)-1
    cols_max = len(matrix[0])-1
    
    while(1):
        if (rows < 0 or cols < 0 or rows > rows_max or cols > cols_max):
            return -1
        check_point = matrix[rows][cols]
        
        if (search_num == check_point):
            return [rows, cols]
        
        elif (search_num < check_point):
            cols = cols-1 # => cols -= 1
        else:
            rows = rows+1 # => rows += 1
            
"""
测试用例
1）二维数组中包含查找的数字（查找的数字是数组中的最大值和最小值，介于两者之间）
2）二维数组中没有查找的数字（或大于最大值，或小于最小值，介于两者之间但是不存在）
3）特殊输入测试
"""
matrix = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print (findNumber(matrix, 7))
print (findNumber(matrix, 15))
print (findNumber(matrix, 1))
print (findNumber(matrix, 0))
print (findNumber(matrix, 16))
print (findNumber(matrix, 11))
print (findNumber(matrix, '2'))