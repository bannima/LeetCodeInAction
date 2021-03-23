#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: backtrace.py
Description: 
Author: Barry Chow
Date: 2021/3/23 9:13 PM
Version: 0.1
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def char_num(num):
            assert num >= 2 and num <= 9
            if num <= 6:
                chars = [chr((num - 1) * 3 + 94 + i) for i in range(3)]

            elif num == 7:
                chars = ['p', 'q', 'r', 's']
            elif num == 8:
                chars = ['t', 'u', 'v']
            elif num == 9:
                chars = ['w', 'x', 'y', 'z']
            return chars

        res = []

        def backtrace(depth, path):
            if depth == len(digits):
                res.append(path)
            elif depth > len(digits):
                return
            else:
                for char in char_num(int(digits[depth])):
                    backtrace(depth + 1, path + char)

        if len(digits) == 0:
            return res
        backtrace(0, "")
        return res

