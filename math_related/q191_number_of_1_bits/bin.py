#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: bin.py
Description: 
Author: Barry Chow
Date: 2021/3/22 2:40 PM
Version: 0.1
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')