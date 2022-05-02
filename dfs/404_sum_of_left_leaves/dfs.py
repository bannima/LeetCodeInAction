#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/5/2 10:31 PM
@desc: 
"""
from typing import List,Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #判断root左子树不为空，且左子树为叶子节点
        res = 0
        if root.left and not root.left.left and not root.left.right:
            res = root.left.val
        return  self.sumOfLeftLeaves(root.left)+ self.sumOfLeftLeaves(root.right) + res