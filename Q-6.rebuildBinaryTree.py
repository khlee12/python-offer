#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 13:14:23 2018

@author: khlee

[面试题6]
输入某二叉树的前序遍历和中序遍历的结果，重建出该二叉树
"""
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
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
   
        
def rebuildBinaryTree(preOrder, inOrder):
    if preOrder is None or not preOrder or inOrder is None or not inOrder:
        return
    rootValue = preOrder[0]
    treeNode = BinaryTreeNode(rootValue)
    rootIndex = 0
    
    for pivot in range(len(inOrder)):
        if inOrder[pivot] == rootValue:
            rootIndex = pivot
            break
    leftChildInOrder = inOrder[0:rootIndex]
    leftChildPreOrder = preOrder[1:1+len(leftChildInOrder)]
    
    rightChildInOrder = inOrder[rootIndex+1:len(inOrder)]
    rightChildPreOrder = preOrder[1+len(leftChildPreOrder):len(preOrder)]
    treeNode.leftChild = rebuildBinaryTree(leftChildPreOrder, leftChildInOrder)
    treeNode.rightChild = rebuildBinaryTree(rightChildPreOrder, rightChildInOrder)
    
    return treeNode
    
    
def unittest(preorder, inorder):
    rebuiltBinaryTree = rebuildBinaryTree(preorder, inorder)
    if rebuiltBinaryTree is None or not rebuiltBinaryTree:
        return
    rebuiltBinaryTree.preOrderTraversal(rebuiltBinaryTree)
    print('-----')
    rebuiltBinaryTree.inOrderTraversal(rebuiltBinaryTree)
    print('-----')
    rebuiltBinaryTree.postOrderTraversal(rebuiltBinaryTree)
    print('*****')
# 测试集
# 不完全二叉树
preorder1 = [1,2,4,7,3,5,6,8]
inorder1 = [4,7,2,1,5,3,8,6]

# 完全二叉树
preorder2 = [1,2,4,7,3,5,8]
inorder2 = [4,2,7,1,5,3,8]
# 4 7 2 5 8 3 1

# 特殊二叉树（所有节点都没有右子节点
preorder3 = [1,2,3,4,5]
inorder3 = [5,4,3,2,1]
# 5 4 3 2 1 

# 特殊二叉树（所有节点都没有左子节点
preorder3 = [1,2,3,4,5]
inorder3 = [1,2,3,4,5]
# 5 4 3 2 1

# 特殊二叉树（只有一个节点
preorder4 = [1]
inorder4 = [1]

# 特殊输入（None
preorder5 = None
inorder5 = None

# 前序遍历与中序遍历不匹配
preorder6 = [1,2,4,7,3,5,6,8]
inorder6 = [4,7,2,1,5,9,8,6]

unittest(preorder1, inorder1)
unittest(preorder2, inorder2)
unittest(preorder3, inorder3)
unittest(preorder4, inorder4)
unittest(preorder5, inorder5)
unittest(preorder6, inorder6)
