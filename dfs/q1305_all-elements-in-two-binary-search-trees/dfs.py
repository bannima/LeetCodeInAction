#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/5/2 11:19 AM
@desc: 
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root,path):
            if root:
                if root.left:
                    dfs(root.left,path)
                path.append(root.val)
                if root.right:
                    dfs(root.right,path)
        path1,path2 = [],[]
        dfs(root1,path1),dfs(root2,path2)
        # merge sort
        res,i,j = [], 0,0
        while(i<len(path1) and j<len(path2)):
            if path1[i]<=path2[j]:
                res.append(path1[i])
                i+=1
            else:
                res.append(path2[j])
                j+=1
        if i<len(path1):
            return res + path1[i:]
        else:
            return res + path2[j:]
