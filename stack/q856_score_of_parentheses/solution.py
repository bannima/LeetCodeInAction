#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/16 10:39 PM
Version: 0.1
"""


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        def isInt(n):
            try:
                n = int(n)
                return True
            except ValueError:
                return False

        stack = []
        S = list(S)
        while len(S) > 0:
            char = S[0]
            del S[0]

            if not stack:
                stack.append(char)
            elif char == ')':
                if isInt(stack[-1]):
                    num = int(stack.pop())
                    # remove (
                    stack.pop()
                    # stack.append(2*num)
                    S = [str(2 * num)] + S
                elif stack[-1] == '(':
                    stack.pop()
                    # stack.append(1)
                    S = [str(1)] + S
            elif isInt(char):
                if isInt(stack[-1]):
                    num = int(stack.pop())
                    # stack.append(isInt(char)+num)
                    S = [str(int(char) + num)] + S
                else:
                    stack.append(char)
            else:
                stack.append(char)

        return int(stack[-1])



