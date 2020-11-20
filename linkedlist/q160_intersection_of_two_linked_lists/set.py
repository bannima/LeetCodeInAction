#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: set.py
Description: 
Author: Barry Chow
Date: 2020/11/20 8:59 PM
Version: 0.1
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_set = set()
        while(headA):
            node_set.add(headA)
            headA = headA.next
        while(headB):
            if headB in node_set:
                return headB
            else:
                headB = headB.next
        return None