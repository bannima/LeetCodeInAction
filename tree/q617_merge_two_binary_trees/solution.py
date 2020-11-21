#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/21 4:49 PM
Version: 0.1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def merge(p, q):
            if p is None and q is None:
                return None
            elif p is None:
                return q
            elif q is None:
                return p
            else:
                node = TreeNode(p.val + q.val)
                node.left = merge(p.left, q.left)
                node.right = merge(p.right, q.right)
                return node

        return merge(t1, t2)
