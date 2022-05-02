#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/5/2 10:24 AM
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
        self.flag = False

        def dfs(root, pathsum):
            # make sure this is leaf node
            if (not root.left and not root.right) and (pathsum + root.val == targetSum):
                self.flag = True
                return
            if root.left:
                dfs(root.left, pathsum + root.val)
            if root.right:
                dfs(root.right, pathsum + root.val)

        if root:
            dfs(root, 0)
        return self.flag
