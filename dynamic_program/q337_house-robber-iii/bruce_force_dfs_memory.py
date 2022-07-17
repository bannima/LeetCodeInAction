#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: bruce_force_dfs_memory.py
@time: 2022/7/17 2:53 PM
@desc: 
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    @cache
    def rob(self, root: TreeNode) -> int:
        # null node
        if not root:
            return 0
        # leaf node
        elif not root.left and not root.right:
            return root.val
        else:
            money = root.val
            if root.left:
                money += self.rob(root.left.left) + self.rob(root.left.right)
            if root.right:
                money += self.rob(root.right.left) + self.rob(root.right.right)
            left_rob = self.rob(root.left)
            right_rob = self.rob(root.right)
            return max(money,left_rob + right_rob)


