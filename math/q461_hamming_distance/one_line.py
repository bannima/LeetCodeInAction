#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: one_line.py
Description: 
Author: Barry Chow
Date: 2020/11/20 8:09 PM
Version: 0.1
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')