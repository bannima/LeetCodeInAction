#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/21 10:38 AM
Version: 0.1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return p.val==q.val and check(p.left,q.right) and check(p.right,q.left)
        return check(root,root)