#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: pre_in_order.py
@time: 2022/5/11 9:28 PM
@desc: 
"""
from typing import List

import json

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import json
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def pre_order(root):
            return [root.val] + pre_order(root.left) + pre_order(root.right) if root else []

        def in_order(root):
            return in_order(root.left) + [root.val] + in_order(root.right) if root else []

        return json.dumps({"pre": pre_order(root), "in": in_order(root)})

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def build_tree(in_order, pre_order):
            root = None
            if len(pre_order) > 0 and len(in_order) > 0:
                root = TreeNode(pre_order[0])
                #
                left_in_order = in_order[:in_order.index(pre_order[0])]
                left_pre_order = pre_order[1:len(left_in_order) + 1]

                right_in_order = in_order[in_order.index(pre_order[0]) + 1:]
                right_pre_order = pre_order[len(left_in_order) + 1:]

                root.left = build_tree(left_in_order, left_pre_order)
                root.right = build_tree(right_in_order, right_pre_order)

                #print(left_in_order, left_pre_order, right_in_order, right_pre_order)
            return root

        data = json.loads(data)
        print(data)
        return build_tree(data["in"], data["pre"])

if __name__ =='__main__':
    ser = Codec()
    deser = Codec()
    tree = '{"pre": [3, 2, 1, 4], "in": [2, 1, 3, 4]}'
    ans = deser.deserialize(tree)
    tree = ser.serialize(ans)
