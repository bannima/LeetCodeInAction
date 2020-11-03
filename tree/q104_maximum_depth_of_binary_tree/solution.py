#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/3 11:12 AM
Version: 0.1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        levels = [0]
        self.maxD(root, 1, levels)
        return max(levels)

    def maxD(self, root, depth, levels):
        if root is None:
            return
        # 叶子节点
        if root.right is None and root.left is None:
            levels.append(depth)
        if root.right is not None:
            self.maxD(root.right, depth + 1, levels)
        if root.left is not None:
            self.maxD(root.left, depth + 1, levels)

