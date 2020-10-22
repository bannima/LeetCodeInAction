#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/22 5:09 PM
Version: 0.1
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        中序遍历二叉树，判断是否为严格升序
        :type root: TreeNode
        :rtype: bool
        """

        ans = []
        self.inOrder(root, ans)
        if len(ans) == 0:
            return True
        for i in range(1, len(ans)):
            if ans[i] <= ans[i - 1]:
                return False
        return True

    def inOrder(self, root, ans):
        if not root:
            return []
        if root.left:
            self.inOrder(root.left, ans)
        ans.append(root.val)
        if root.right:
            self.inOrder(root.right, ans)

        return ans



