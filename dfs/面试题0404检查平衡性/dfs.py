#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/5/3 10:21 AM
@desc: 
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True

        # return the tree height
        def tree_height(root):
            if not root:
                return 0
            # leaf node
            if not root.left and not root.right:
                return 1
            left_h = tree_height(root.left) + 1
            right_h = tree_height(root.right) + 1
            if abs(left_h - right_h) > 1:
                self.flag = False
            return max(left_h, right_h)

        tree_height(root)
        return self.flag


