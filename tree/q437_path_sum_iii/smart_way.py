#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: smart_way.py
Description: 
Author: Barry Chow
Date: 2020/11/6 11:36 AM
Version: 0.1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        '''巧妙在于不用保存路径，只保存到当前节点所有可能路径的和'''
        def dfs(root,sumList):
            if root is None:
                return 0
            sumList = [val+root.val for val in sumList]+[root.val]
            res = sumList.count(sum)
            return res+dfs(root.left,sumList)+dfs(root.right,sumList)

        return dfs(root,[])