#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: recurisive.py
@time: 2022/5/16 4:10 PM
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left_n = self.findChild(root.left)
        if left_n == k - 1:
            return root.val
        elif left_n >= k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - 1 - left_n)

    def findChild(self, node):
        if not node: return 0
        return self.findChild(node.left) + 1 + self.findChild(node.right)