#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/16 9:03 PM
Version: 0.1
"""


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_v = float('inf')
        max_v = float('-inf')
        min_max = []
        for v in nums:
            for mi_v, ma_v in min_max:
                if v < ma_v and v > mi_v: return True
            if v < min_v:
                min_v = v
                max_v = float('-inf')
            max_v = max(max_v, v)
            if min_v < max_v: min_max.append([min_v, max_v])
        return False