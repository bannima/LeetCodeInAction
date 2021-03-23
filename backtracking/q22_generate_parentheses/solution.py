#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/3/23 9:53 PM
Version: 0.1
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = ['(', ')']
        res = []

        def is_legal(path):

            stack = []
            for v in path:
                if not len(stack):
                    stack.append(v)
                else:
                    if stack[-1] == '(' and v == ")":
                        stack.pop()
                    else:
                        stack.append(v)
            if len(stack):
                return False
            return True

        def backtrace(depth, path):
            if depth == n * 2:
                if is_legal(path):
                    res.append(path)
            else:
                for brack in brackets:
                    backtrace(depth + 1, path + brack)

        backtrace(0, "")
        return res


