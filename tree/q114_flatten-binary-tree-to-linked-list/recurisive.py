#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: recurisive.py
@time: 2022/5/12 6:04 PM
@desc: 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # none
        if not root:
            return None
        # leaf node
        if not root.left and not root.right:
            return root
        left_node = self.flatten(root.left)
        right_node = self.flatten(root.right)
        # has left
        if left_node:
            root.right = left_node
            # to the left end
            while (left_node.right): left_node = left_node.right
            left_node.right = right_node
        root.left = None
        return root



