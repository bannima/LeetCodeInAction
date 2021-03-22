#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: logn.py
Description: 
Author: Barry Chow
Date: 2021/3/22 2:43 PM
Version: 0.1
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res += 1
            n = n &(n-1)
        return res