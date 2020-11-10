#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/10 6:27 PM
Version: 0.1
"""
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','{':'}','[':']'}
        stack = []
        for char in s:
            if len(stack)==0:
                stack.append(char)
            else:
                if char==dic.get(stack[-1]):
                    stack.pop()
                else:
                    stack.append(char)

        return len(stack)==0