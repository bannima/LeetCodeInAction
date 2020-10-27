#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/27 8:13 AM
Version: 0.1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

