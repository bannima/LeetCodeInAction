#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/9 10:58 PM
Version: 0.1
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0 or len(popped) == 0:
            return True
        stack = []
        i = j = 0
        while (j < len(popped)):
            if len(stack) == 0:
                stack.append(pushed[i])
                i += 1
            elif stack[-1] != popped[j]:
                if i < len(pushed):
                    stack.append(pushed[i])
                else:
                    break
                i += 1
            else:
                stack.pop()
                j += 1

        return len(stack) == 0


