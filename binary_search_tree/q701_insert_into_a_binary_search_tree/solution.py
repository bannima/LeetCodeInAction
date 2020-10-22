#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/22 4:40 PM
Version: 0.1
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        copy = root
        if not root:
            return TreeNode(val)
        while root:
            #在左子树
            if val<root.val:
                #左子树不为空，下移
                if root.left:
                    root = root.left
                #左子树为空，新建节点
                else:
                    root.left = TreeNode(val)
                    break
            #右子树
            else:
                #右子树不为空，下移
                if root.right:
                    root = root.right
                #右子树为空，插入节点
                else:
                    root.right = TreeNode(val)
                    break

        return copy
