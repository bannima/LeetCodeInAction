#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/11 9:33 AM
Version: 0.1
"""

class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while(num>=10):
            res = 0
            while(num):
                res += num %10
                num = num//10
            num = res
        return num
