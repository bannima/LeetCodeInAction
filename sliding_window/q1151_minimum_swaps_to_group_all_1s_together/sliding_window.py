#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/21 3:58 PM
Version: 0.1
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        s = sum(data)
        r = 0
        count_one = sum(data[0:s])
        times = s-count_one
        while r<len(data)-s:
            count_one += data[r+s]
            count_one -= data[r]
            times = min(times,s-count_one)
            r+=1
        return times
