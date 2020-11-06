#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/6 11:30 AM
Version: 0.1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        res = 0
        if not root:
            return res

        queue = deque()
        path = [root.val]
        queue.append((root, path))

        while queue:
            node, path = queue.popleft()
            # 对于path，计算到node为止是否有路径等于target

            for i in range(len(path)):
                if sum(path[i:]) == target:
                    res += 1

            if node.left:
                path_l = copy.copy(path)
                path_l.append(node.left.val)
                queue.append((node.left, path_l))

            if node.right:
                path_r = copy.copy(path)
                path_r.append(node.right.val)
                queue.append((node.right, path_r))
        return res



