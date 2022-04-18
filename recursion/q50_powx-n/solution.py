#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/4/18 8:30 PM
@desc: 
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        abs_n = abs(n)
        if abs_n % 2 == 0:
            t = self.myPow(x, abs_n // 2)
            x = t * t
        else:
            t = self.myPow(x, abs_n // 2)
            x = t * t * x
        if n < 0:
            x = 1.0 / x
        return x
