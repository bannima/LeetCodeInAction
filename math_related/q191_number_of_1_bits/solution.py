#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/3/22 2:29 PM
Version: 0.1
"""

class Solution:
    def hammingWeight(self, n):
        res = sum([1 for i in range(32) if (1<<i) & n])
        return res

