#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: xor.py
Description: 
Author: Barry Chow
Date: 2020/11/20 8:04 PM
Version: 0.1
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = bin(x)[2:]
        by = bin(y)[2:]
        if x>y:
            by = '0'*(len(bx)-len(by))+by
        else:
            bx = '0'*(len(by)-len(bx))+bx
        res = 0
        for i,j in zip(bx,by):
            res += int(i) ^ int(j)
        return res
