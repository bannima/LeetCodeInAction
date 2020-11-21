#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/21 10:06 AM
Version: 0.1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(root):
            if root is None: return
            root.left,root.right = root.right,root.left
            if root.left is not None:
                invert(root.left)
            if root.right is not None:
                invert(root.right)
        invert(root)
        return root
