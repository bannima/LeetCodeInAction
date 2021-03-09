#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: stack.py
Description: 
Author: Barry Chow
Date: 2021/3/9 9:49 AM
Version: 0.1
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if len(stack)>0 and stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)