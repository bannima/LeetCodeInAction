#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/12 7:55 PM
Version: 0.1
"""


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = even = 0
        res = []
        while odd < len(A) and even < len(A):
            # locate odd and even
            while A[odd] % 2 != 0: odd += 1
            res.append(A[odd])
            odd += 1

            while A[even] % 2 != 1: even += 1
            res.append(A[even])
            even += 1
        return res