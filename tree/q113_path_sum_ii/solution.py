#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/6 10:39 AM
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
        res = []
        paths = []
        self.pathS(root, paths, sum, res)
        return res

    def pathS(self, root, paths, target, res):
        if not root:
            return
        # 叶子节点
        if not root.left and not root.right:
            if sum(paths) + root.val == target:
                paths.append(root.val)
                res.append(paths)
        # 左子树不为空
        if root.left:
            path_l = copy.copy(paths)
            path_l.append(root.val)
            self.pathS(root.left, path_l, target, res)
        # 右子树不为空
        if root.right:
            path_r = copy.copy(paths)
            path_r.append(root.val)
            self.pathS(root.right, path_r, target, res)




