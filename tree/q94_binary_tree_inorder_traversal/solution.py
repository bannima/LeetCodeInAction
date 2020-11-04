#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/4 10:51 AM
Version: 0.1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorderT(root,res)
        return res

    def inorderT(self,root,res):
        if root:
            if root.left:
                self.inorderT(root.left,res)
            res.append(root.val)
            if root.right:
                self.inorderT(root.right,res)