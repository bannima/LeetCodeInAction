#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/4 3:13 PM
Version: 0.1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        res = []
        tmp = []
        cur_depth = 0

        for node, depth in queue:
            if node:

                if cur_depth != depth:
                    cur_depth = depth
                    res.append(tmp)
                    tmp = []
                tmp.append(node.val)

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        res.append(tmp)
        return list(reversed(res))