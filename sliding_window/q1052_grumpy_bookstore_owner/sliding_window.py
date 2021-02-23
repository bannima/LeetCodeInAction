#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/23 11:03 AM
Version: 0.1
"""


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        def sum_arr(a, b):
            s = 0
            for c, g in zip(a, b):
                s += c * (1 - g)
            return s

        s = sum_arr(customers, grumpy)

        tmp = 0
        l = r = 0
        max_tmp = 0
        while r < len(customers):
            if r < X:
                tmp += customers[r] * grumpy[r]
            else:
                tmp -= customers[l] * grumpy[l]
                tmp += customers[r] * grumpy[r]
                l += 1
            max_tmp = max(max_tmp, tmp)
            r += 1

        return s + max_tmp




