#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/4 3:41 PM
Version: 0.1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        res = []
        flag = True
        while len(queue):
            tmp = []
            size = len(queue)
            for _ in range(size):

                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            tmp = tmp if flag else tmp[::-1]
            res.append(tmp)
            if flag:
                flag = False
            else:
                flag = True
        return res