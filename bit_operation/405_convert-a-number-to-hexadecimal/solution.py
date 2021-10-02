#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/10/2 4:30 PM
Version: 0.1
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        hex = '0123456789abcdef'
        ans = ''
        while (num != 0 and len(ans) < 8):
            ans = hex[num & 0xf] + ans
            num >>= 4
        return ans



