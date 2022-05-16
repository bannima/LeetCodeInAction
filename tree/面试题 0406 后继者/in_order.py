#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: in_order.py
@time: 2022/5/16 3:17 PM
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
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if not root:return None
        if root.val<=p.val:return self.inorderSuccessor(root.right,p)
        ans = self.inorderSuccessor(root.left,p)
        return ans if ans else root