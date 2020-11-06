#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/6 1:29 PM
Version: 0.1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_v = float('-inf')

    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(root, maximum, minimum):
            if root:
                maximum = max(root.val, maximum)
                minimum = min(root.val, minimum)
                tmp = max(abs(maximum - root.val), abs(minimum - root.val))
                self.max_v = max(self.max_v, tmp)
                dfs(root.left, maximum, minimum)
                dfs(root.right, maximum, minimum)

        dfs(root, float('-inf'), float('inf'))
        return self.max_v
