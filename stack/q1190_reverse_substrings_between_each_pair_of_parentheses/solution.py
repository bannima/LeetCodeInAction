#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/16 9:49 PM
Version: 0.1
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char==')':
                tmp = []
                #in stack
                while stack:
                    element = stack.pop()
                    if element=='(':break
                    else:
                        tmp.append(element)
                #out stack
                for element in tmp:
                    stack.append(element)
            else:
                stack.append(char)
        return ''.join(stack)