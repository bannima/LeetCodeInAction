#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/18 4:03 PM
Version: 0.1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #返回树的最大深度，和经过该节点的最大直径
        def tree_depth_diam(root,depth):
            if root is None:
                return depth,0
            else:
                left_depth,left_diam = tree_depth_diam(root.left,depth)
                right_depth,right_diam = tree_depth_diam(root.right,depth)
                depth = max(left_depth,right_depth)+1
                diam = max(left_depth+right_depth,left_diam,right_diam)
                return depth,diam

        if not root:
            return 0
        else:
            depth,diam = tree_depth_diam(root,0)
            return diam