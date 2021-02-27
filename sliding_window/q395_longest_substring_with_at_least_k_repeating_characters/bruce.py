#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: bruce.py
Description: 
Author: Barry Chow
Date: 2021/2/27 3:31 PM
Version: 0.1
"""

from collections import Counter

class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        def check(sc):
            for v in sc.values():
                if v <k:
                    return False
            return True
        max_len = 0
        if len(s)<=1:
            return 1 if k<=1 else 0
        for i in range(len(s)):
            sc = Counter(s[i])
            for j in range(i+1,len(s)):
                sc.update(s[j])
                if check(sc):
                    max_len = max(max_len,j-i+1)
        return max_len

