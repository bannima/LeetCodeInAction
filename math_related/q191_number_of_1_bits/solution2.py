#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution2.py
Description: 
Author: Barry Chow
Date: 2021/3/22 2:41 PM
Version: 0.1
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n!=0:
            res += n & 1
            n = n >> 1
        return res