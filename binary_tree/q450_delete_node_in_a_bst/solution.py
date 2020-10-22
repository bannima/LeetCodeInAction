#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/22 4:04 PM
Version: 0.1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    #查找root的后继节点
    def succesor(self,root):
        root = root.right
        while root.left:
            root = root.left
        return root

    #查找root的先继节点
    def presuccesor(self,root):
        root = root.left
        while root.right:
            root = root.right
        return root


    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        return self.del_node(root,key)
        #return root

    def del_node(self,root,key):
        if not root:
            return None

        if root.val==key:
            #叶子节点，直接删除
            if root.left==None and root.right==None:
                root = None
            #右子树不为空，用root的后继节点值覆盖其root，在右子树中递归删除该后继节点
            elif root.right!=None:
                root.val = self.succesor(root).val
                root.right = self.del_node(root.right,self.succesor(root).val)
            #右子树为空，左子树不为空，删除前继节点，在左子树中递归删除该前继节点
            else:
                root.val = self.presuccesor(root).val
                root.left = self.del_node(root.left,self.presuccesor(root).val)

        elif root.val>key:
            root.left = self.del_node(root.left,key)
        else:
            root.right = self.del_node(root.right,key)

        return root

