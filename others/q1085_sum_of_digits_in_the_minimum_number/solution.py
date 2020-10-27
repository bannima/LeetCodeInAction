#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/27 10:11 AM
Version: 0.1
"""


class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        min_num = A[0]
        for j in range(1, len(A)):
            if A[j] < min_num:
                min_num = A[j]
        res = 0
        while (min_num != 0):
            res += min_num % 10
            min_num = int(min_num / 10)
        return 1 if res % 2 == 0 else 0