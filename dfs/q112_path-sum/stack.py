#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: stack.py
@time: 2022/5/2 10:41 AM
@desc: 
"""
from typing import Optional
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        if root:
            stack.append((root,root.val))
        while stack:
            node,path_sum = stack.pop()
            if (not node.left and not node.right) and path_sum==targetSum:
                return True
            if node.left:
                stack.append((node.left,node.left.val+path_sum))
            if node.right:
                stack.append((node.right,node.right.val+path_sum))
        return False