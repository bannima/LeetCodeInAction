#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val<low:
            return self.trimBST(root.right,low,high)
        elif root.val>high:
            return self.trimBST(root.left,low,high)
        else:
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
            return root
