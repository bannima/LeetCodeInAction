#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/4 11:27 AM
Version: 0.1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.treeDepth(root.left) - self.treeDepth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def treeDepth(self, root):
        if root is None:
            return 0
        return max(self.treeDepth(root.left), self.treeDepth(root.right)) + 1

