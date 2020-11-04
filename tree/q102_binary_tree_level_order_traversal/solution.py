#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/4 10:26 AM
Version: 0.1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''层次遍历，保留depth深度信息'''
        if root is None:
            return []

        depth =0
        cur_depth = 0
        queue = [(root,depth)]
        res = []
        tmp = []
        for node,depth in queue:
            if node:
                if cur_depth!=depth:
                    cur_depth=depth
                    res.append(tmp)
                    tmp = []
                tmp.append(node.val)
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        res.append(tmp)

        return res