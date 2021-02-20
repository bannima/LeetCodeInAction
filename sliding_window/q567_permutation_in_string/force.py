#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: force.py
Description: 
Author: Barry Chow
Date: 2021/2/20 6:00 PM
Version: 0.1
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def equals(a, b):
            a = list(a)
            a.sort()
            b = list(b)
            b.sort()
            return a == b

        n1 = len(s1)
        n2 = len(s2)
        for i in range(n2 - n1 + 1):
            if equals(s2[i:i + n1], s1):
                return True
        return False

