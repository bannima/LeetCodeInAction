#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/4 4:14 PM
Version: 0.1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #min_depth = float('inf')
        return self.minD(root)

    def minD(self,root):
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minD(root.left),self.minD(root.right))+1
        elif root.left:
            return self.minD(root.left)+1
        else:
            return self.minD(root.right)+1
