#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/5/2 10:34 AM
@desc: 
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #节点为空，返回false
        if not root:
            return False
        #若为叶子结点，返回该叶子结点值，是否等于target
        if not root.left and not root.right:
            return root.val==targetSum
        # 遍历左子树，或者右子树，若有一个为True即可
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)