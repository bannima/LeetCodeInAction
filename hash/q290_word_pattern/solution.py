#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/16 10:30 AM
Version: 0.1
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s)!= len(pattern): return False
        dic = {}
        for p,si in zip(pattern,s):
            if p in dic:
                if dic[p]!=si: return False
            elif si in dic.values():
                return False
            else:
                dic[p] = si
        return True
