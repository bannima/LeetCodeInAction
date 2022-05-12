#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/12 8:47 PM
@desc: 
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_v = float("-inf")
        def max_gain(node):
            """返回改节点的最大收益"""
            if not node:
                return 0
            else:
                left = max(max_gain(node.left),0)
                right = max(max_gain(node.right),0)
                node_gain = left + right + node.val
                self.max_v = max(self.max_v,node_gain)
            return node.val + max(left,right) #
        max_gain(root)
        return self.max_v