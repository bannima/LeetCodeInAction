#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/13 9:05 AM
Version: 0.1
"""


class Solution:
    def decodeString(self, s: str) -> str:
        def isInt(char):
            try:
                val = int(char)
                return True
            except ValueError:
                return False

        def popElem():
            nonlocal stack

            index = len(stack) - 1
            while (stack[index] != '['): index -= 1
            s_part = ''.join(stack[index + 1:])
            stack = stack[:index]

            index = len(stack) - 1
            while (index >= 0 and isInt(stack[index])): index -= 1
            n = int(''.join(stack[index + 1:]))
            stack = stack[:index + 1]

            stack.append(n * s_part)

        stack = []
        res = ''
        for char in s:
            if char == ']':
                stack.append(popElem())
            else:
                stack.append(char)
        return ''.join(stack)