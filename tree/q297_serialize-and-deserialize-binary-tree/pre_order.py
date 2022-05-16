#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: pre_order.py
@time: 2022/5/16 5:23 PM
@desc: 
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import json


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def pre_order(node):
            return [node.val] + pre_order(node.left) + pre_order(node.right) if node else [None]

        return json.dumps(pre_order(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        pre_order = json.loads(data)
        print(pre_order)

        def construct(path):
            val = path.pop(0)
            if val == None:
                return None
            node = TreeNode(val)
            node.left = construct(path)
            node.right = construct(path)
            return node

        root = construct(pre_order)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))