#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/9 9:38 PM
Version: 0.1
"""
from math import sqrt,pow
class Solution:
    def isHappy(self, n: int) -> bool:
        def calc(num):
            res=0
            while(num):
                res += pow(num%10,2)
                num = num//10
            return res
        slow = n
        fast = n
        while True:
            slow = calc(slow)
            fast = calc(fast)
            fast = calc(fast)
            if fast==slow: break
        return slow==1