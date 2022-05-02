#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: queue.py
@time: 2022/5/2 10:42 AM
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = []
        if root:
            queue.append((root,root.val))
        while queue:
            node,path_sum = queue.pop(0)
            if (not node.left and not node.right) and path_sum==targetSum:
                return True
            if node.left:
                queue.append((node.left,node.left.val+path_sum))
            if node.right:
                queue.append((node.right,node.right.val+path_sum))
        return False