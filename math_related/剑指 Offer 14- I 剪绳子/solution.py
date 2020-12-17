#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/17 8:50 PM
Version: 0.1
"""

class Solution:
    def cuttingRope(self, n: int) -> int:
        #投机取巧，发现取3最划算
        if n<=3: return n-1
        s = n//3
        if n%3==0:
            return pow(3,s)
        elif n%3==1:
            return pow(3,s-1)*(n%3+3)
        else:
            return pow(3,s)*(n%3)