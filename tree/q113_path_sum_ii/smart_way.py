#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: smart_way.py
Description: 
Author: Barry Chow
Date: 2020/11/6 11:51 AM
Version: 0.1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        path = []
        res = []

        def dfs(root,total):
            if root is None:
                return
            path.append(root.val)
            if not root.left and not root.right and root.val==total:
                res.append(copy.copy(path))
            total -= root.val
            dfs(root.left,total)
            dfs(root.right,total)

            path.pop()
            total+=root.val

        dfs(root,sum)

        return res
