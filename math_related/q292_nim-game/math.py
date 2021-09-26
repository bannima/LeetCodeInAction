#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: math.py
Description: 
Author: Barry Chow
Date: 2021/9/26 10:20 PM
Version: 0.1
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return not n%4==0