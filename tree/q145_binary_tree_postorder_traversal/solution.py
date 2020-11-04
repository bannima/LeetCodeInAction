#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/4 10:46 AM
Version: 0.1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postorderT(root,res)
        return res

    def postorderT(self,root,res):
        if root is None:
            return
        if root.left:
            self.postorderT(root.left,res)
        if root.right:
            self.postorderT(root.right,res)
        res.append(root.val)
