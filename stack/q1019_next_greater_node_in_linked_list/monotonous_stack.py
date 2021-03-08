#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: monotonous_stack.py
Description: 
Author: Barry Chow
Date: 2021/3/8 3:11 PM
Version: 0.1
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        pos = {}
        # 单调栈
        stack = []
        keys = []
        i = 0
        while (head):
            keys.append(head.val)
            if len(stack) == 0:
                stack.append(i)
            else:
                while (len(stack) > 0 and keys[stack[-1]] < head.val):
                    pos[stack.pop()] = head.val
                stack.append(i)

            head = head.next
            i += 1
        answer = [0] * len(keys)
        for i in pos:
            answer[i] = pos[i]

        return answer
