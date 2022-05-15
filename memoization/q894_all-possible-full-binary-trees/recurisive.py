#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: recurisive.py
@time: 2022/5/15 4:25 PM
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
    map = {0:[],1:[TreeNode(val=0)]}
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n not in Solution.map:
            ans = []
            for i in range(n):
                left = n-1-i
                for l in self.allPossibleFBT(i):
                    for r in self.allPossibleFBT(n-i-1):
                        node = TreeNode(val=0,left=l,right=r)
                        ans.append(node)
            Solution.map[n] = ans
        return Solution.map[n]

