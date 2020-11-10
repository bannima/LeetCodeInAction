#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/10 10:16 PM
Version: 0.1
"""


class Solution:
    def calculate(self, s: str) -> int:
        '''
        考虑清楚各种分支情况，入栈出栈的条件
        '''
        def calc(a, b, c):
            if b == '+':
                return str(int(a) + int(c))
            else:
                return str(int(a) - int(c))

        def isInt(z):
            try:
                z_handle = int(z)
                return isinstance(z_handle, int)
            except ValueError:
                return False

        def isSymbol(char):
            return char in ['+', '-']

        stack = [];
        res = 0
        for char in s + 'e':
            if char == ' ': continue
            if char == ')':
                if len(stack) > 2 and isSymbol(stack[-2]):
                    c = stack.pop()
                    b = stack.pop()
                    a = stack.pop()
                    # remove (
                    stack.pop()
                    stack.append(calc(a, b, c))
                elif stack[-2] == '(':
                    del stack[-2]
            # is number
            elif isInt(char):
                if len(stack) == 0:
                    stack.append(char)
                # 两位数或多位数字的情况
                elif isInt(stack[-1]):
                    stack.append(str(int(stack.pop()) * 10 + int(char)))
                else:
                    stack.append(char)
            elif isSymbol(char):
                if len(stack) >= 2 and isSymbol(stack[-2]):
                    c = stack.pop()
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(calc(a, b, c))
                stack.append(char)
            # end of str s
            elif char == 'e':
                if len(stack) == 3:
                    c = stack.pop()
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(calc(a, b, c))
            else:
                stack.append(char)
        res = 0
        for num in stack:
            res = res * 10 + int(num)
        return res











