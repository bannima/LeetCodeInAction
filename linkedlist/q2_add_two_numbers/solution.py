#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/9/1 8:46 PM
Version: 0.1
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode()
        cur = root
        addition = 0 #进位
        while True:
            if l1 and l2:
                s = l1.val+l2.val+addition
            elif l1:
                s = l1.val+addition
            elif l2:
                s = l2.val+addition
            else:
                if addition==1:
                    cur.next = ListNode(val=addition)
                    cur = cur.next
                return root.next
            addition =s//10
            cur.next = ListNode(val=s%10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
