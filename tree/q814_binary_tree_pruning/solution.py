#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/6 8:34 PM
Version: 0.1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def containOnes(node):
            '''以node为根的子树是否包含1，若左右子树包含，则去掉左右子树'''
            if not node: return False
            left = containOnes(node.left)
            right = containOnes(node.right)
            if left == False: node.left = None
            if right == False: node.right = None
            return node.val == 1 or left or right

        return root if containOnes(root) else None


