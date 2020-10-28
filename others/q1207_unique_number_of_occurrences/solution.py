#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/28 9:47 AM
Version: 0.1
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dicts = {}
        for num in arr:
            if num in dicts:
                dicts[num] += 1
            else:
                dicts[num] = 1
        freqs = dicts.values()
        dicts = {}
        for freq in freqs:
            if freq in dicts:
                return False
            else:
                dicts[freq] = 1
        return True
