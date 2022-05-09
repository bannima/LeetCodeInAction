#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: greedy.py
@time: 2022/1/15 8:38 PM
@desc: 
"""


class Solution:
    def maximumGain(self, s, x, y):
        res = 0

        def count(s, target, score):
            nonlocal res
            stack = []
            for i in range(len(s)):
                if stack and stack[-1] + s[i] == target:
                    stack.pop()
                    res += score
                else:
                    stack.append(s[i])
            return stack
        if x > y:#贪心找全部最大的字符串进行匹配，然后再找剩下的字符串进行匹配
            stack = count(s, 'ab', x)
            count(stack, 'ba', y)
        else:
            stack = count(s, 'ba', y)
            count(stack, 'ab', x)
        return res