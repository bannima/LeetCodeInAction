#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/9/25 10:38 AM
Version: 0.1
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        nodes = []
        def inOrderTraverse(node):
            if not node:
                return
            nodes.append(node)
            if node.child:
                inOrderTraverse(node.child)
            if node.next:
                inOrderTraverse(node.next)
        inOrderTraverse(head)
        print([n.val for n in nodes])
        if len(nodes)==0:
            return None
        root = nodes[0]
        for i in range(1,len(nodes)):
            nodes[i].prev = nodes[i-1]
            nodes[i-1].next = nodes[i]
            nodes[i].child=None
            nodes[i-1].child=None

        return root



