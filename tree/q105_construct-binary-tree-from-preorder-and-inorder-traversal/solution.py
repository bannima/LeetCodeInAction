#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/4/29 11:21 AM
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        elif len(preorder)==1:
            return TreeNode(val=preorder[0])
        else:
            root = TreeNode(val=preorder[0])
            root_index = inorder.index(preorder[0])

            root.left = self.buildTree(preorder[1:root_index+1],inorder[:root_index])

            root.right = self.buildTree(preorder[1+root_index:],inorder[root_index+1:])

            return root