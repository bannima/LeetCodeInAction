#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/9 9:59 PM
Version: 0.1
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #快慢指针法
        fast = head
        slow = head
        while(fast.next):
            fast = fast.next
            #对于fast指针走不完两步，卡在第二步的情况
            if fast.next is None:
                slow = slow.next
                break
            fast =fast.next
            slow = slow.next
        return slow

