#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:53:25 2019

@author: khlee
"""

# Graph
'''
represent a graph in memory(pros & cons)
https://stackoverflow.com/questions/3287003/three-ways-to-store-a-graph-in-memory-advantages-and-disadvantages
1. Nodes as objects and edges as pointers
2. A matrix containing all edge weights between numbered node x and node y
3. A list of edges between numbered nodes

One way to analyze these is in terms of memory and time complexity (which depends on how you want to access the graph).

**Storing nodes as objects with pointers to one another**
1) The memory complexity for this approach is O(n) because you have as many objects as you have nodes. 
The number of pointers (to nodes) required is up to O(n^2) as each node object may contain pointers for up to n nodes.
2) The time complexity for this data structure is O(n) for accessing any given node.

**Storing a matrix of edge weights**
1) This would be a memory complexity of O(n^2) for the matrix.
2) The advantage with this data structure is that the time complexity to access any given node is O(1).
'''

# traversal
# 实现无向图的深度遍历与广度遍历
# 时间复杂度 O(n2)
        
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']
         }


def dfs(graph, start, visited=None):
    if visited== None:
        visited=[]
    visited.append(start)
    for children in graph[start]:
        if not children in visited:
            dfs(graph, children, visited)
    return visited

print(dfs(graph, 'A'))

from queue import Queue
def bfs(graph, start, visited=None):
    q = Queue()
    if visited == None:
        visited = []
    visited.append(start)
    q.put(start)
    
    while not q.empty():
        node = q.get()
        for children in graph[node]:
            if not children in visited:
                visited.append(children) # visit
                q.put(children)
            
    return visited

print(bfs(graph, 'A'))

# 实现有向图的最短路径算法Dijkstra算法
graph = [
        [0, 10, None, 30, 100],
        [None, 0, 50, None, None],
        [None, None, 0, None, 10],
        [None, None, 20, 0, 60],
        [None, None, None, None, 0]
        ]
# def dijkstra
'''
如何选择合适的遍历算法

DFS和BFS的时间复杂度是相同的，没有优劣之分，只是视不同情况选择不同算法。 
深度优先算法适合目标比较明确，以找到目标为主要目的的情况； 
广度优先算法适合在不断扩大遍历范围时找到相对最优解的情况。

在图中：

**如果按边的权重寻找**：
比如最短路径之类的问题，首先找到距离起始点权重为1的点，之后找到权重为2的点…以此类推直至选找到最短的距离，这实质上就是BFS的一种变形。
**如果按邻接点寻找**： 
比如寻找迷宫，只有一条到达出口的路径，这样的话，通过一个结点，在以这个结点为出发点进行类似操作…直至寻找到出口。即通过DFS的方法。
'''

###########################################
#          分割线            
###########################################

# Tree
# 遍历算法:
# 1) BFS： 广度优先遍历
# 2) DFS： 深度优先遍历（preorder, inorder, postorder）
# 二叉搜索树节点的插入与删除
# trie-tree
# 平衡二叉树（red/black tree)
from queue import Queue

class BinaryTreeNode:
    value = None
    leftChild = None
    rightChild = None
    
    def __init__(self, value, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild

class BinaryTree:
    def preOrderTraversal(self, tree):
        if tree is None:
            return
        print(tree.value)
        self.preOrderTraversal(tree.leftChild)
        self.preOrderTraversal(tree.rightChild)
    def inOrderTraversal(self, tree):
        if tree is None:
            return
        self.inOrderTraversal(tree.leftChild)
        print(tree.value)
        self.inOrderTraversal(tree.rightChild)
    def postOrderTraversal(self, tree):
        if tree is None:
            return
        self.postOrderTraversal(tree.leftChild)
        self.postOrderTraversal(tree.rightChild)
        print(tree.value)
        
    def bfsTraversal(self, tree):
        if tree is None:
            return
        q = Queue()
        q.put(tree)
        while not q.empty():
            node = q.get()
            print(node.value)
            if not node.leftChild is None:
                q.put(node.leftChild)
            if not node.rightChild is None:
                q.put(node.rightChild)

node2 = BinaryTreeNode(8)
node6 = BinaryTreeNode(13)
node3 = BinaryTreeNode(10, leftChild=node2, rightChild=node6)
node4 = BinaryTreeNode(1)
node5 = BinaryTreeNode(5, leftChild=node4)
root = BinaryTreeNode(7, leftChild=node5, rightChild=node3)
tree = BinaryTree()   

print(tree.preOrderTraversal(root))
print(tree.bfsTraversal(root))
    
###########################################
#          分割线            
###########################################
# Sort
# 快速排序 * 在最坏的情况下，待排序的序列为正序或者逆序，每次划分只得到一个比上一次划分少一个记录的子序列，注意另一个为空
# 快速排序改进算法
# 归并排序 * 归并排序的运行时间不依赖待排序元素序列的初始排列，这样他就避免了快排的最差情况
# 插入排序 * 适合用链表结构实现
# 冒泡排序

def quickSort(array, left, right):
    if left >= right:
        return
    pivot = partition(array, left, right)
    quickSort(array, left, pivot - 1)
    quickSort(array, pivot + 1, right)
        
        
def partition(array, left, right):
    key = array[left]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    #left and right meet 
    array[right] = key
    return left

def mergeSort(array):
    if len(array) <= 1:
        return
    mid = len(array)//2
    lefthalf = array[:mid]
    righthalf = array[mid:]
    mergeSort(lefthalf)
    mergeSort(righthalf)
    merge(array, lefthalf, righthalf)

def merge(array, lefthalf, righthalf):
    lPointer = 0
    rPointer= 0
    aPointer = 0
    # 从头开始比较左右子序列的每一个元素，将较小的那一方放入原数组里
    while lPointer < len(lefthalf) and rPointer < len(righthalf):
        if lefthalf[lPointer] < righthalf[rPointer]:
            array[aPointer] = lefthalf[lPointer]
            lPointer += 1
        else:
            array[aPointer] = righthalf[rPointer]
            rPointer += 1
        aPointer += 1
    
    # if there's any element left
    while lPointer < len(lefthalf):
        array[aPointer] = lefthalf[lPointer]
        aPointer += 1
        lPointer += 1
    
    while rPointer < len(righthalf):
        array[aPointer] = righthalf[rPointer]
        aPointer += 1
        rPointer += 1
    
def insertSort(array):
    # 选择一个元素，之前的元素中只要有大于当前值的元素，右移
    for i in range(1, len(array)):
        element = array[i]
        position = i
        
        while position > 0 and array[position-1] > element:
            # move to right
            array[position] = array[position-1]
            position -= 1
        
        array[position] = element               
        
def bubbleSort(array):
    size = len(array)-1
    count = 0
    # 控制循环次数
    for i in range(size):
        # 控制每次循环的子序列长度
        for j in range(size-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                count += 1
        if count == 0:
            # already sorted
            return   
        
array= [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(array, 0, len(array)-1)
print(array)
array= [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(array)
print(array)
array= [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertSort(array)
print(array)
array= [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(array)
print(array)
    
###########################################
#          分割线            
###########################################
# 二分查找

###########################################
#          分割线            
###########################################
'''
power of 2
2的8次方：256
2的10次方：1024
2的16次方：65536
'''
# 位操作


###########################################
#          分割线            
###########################################
# 经典题目
# Towers of Hanoi
# Shortest path problem
# Traveling Salesman problem
# Knapsack problem





