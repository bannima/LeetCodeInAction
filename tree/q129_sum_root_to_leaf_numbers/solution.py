#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/3 9:51 AM
Version: 0.1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        s = []
        self.sumTree(root,0,s)
        return sum(s)

    def sumTree(self,root,parent_val,s):
        if root is None:
            return

        #leaf node
        if root.left is None and root.right is None:
            s.append(parent_val*10+root.val)
        #not leaf node
        if root.left is not None:
            self.sumTree(root.left,parent_val*10+root.val,s)
        if root.right is not None:
            self.sumTree(root.right,parent_val*10+root.val,s)