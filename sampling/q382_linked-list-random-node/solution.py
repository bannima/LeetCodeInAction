#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/1/16 10:24 AM
@desc: 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head):
         self.head = head

    def getRandom(self):
        count = 0
        reserver = 0
        cur = self.head
        while cur:
            count +=1
            rand = random.randint(1,count)
            if rand == count:
                reserver = cur.val
            cur = cur.next
        return reserver