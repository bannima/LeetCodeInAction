#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/9 7:43 PM
Version: 0.1
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        i = 0
        while (fast.next):
            fast = fast.next
            i += 1
            if i == n: break

        if i == n - 1: return head.next
        while (fast.next):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head