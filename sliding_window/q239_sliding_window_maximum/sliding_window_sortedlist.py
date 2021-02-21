#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window_sortedlist.py
Description: 
Author: Barry Chow
Date: 2021/2/21 11:16 AM
Version: 0.1
"""

from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = SortedList()
        l = r = 0
        res = []

        while(r<len(nums)):
            window.add(nums[r])
            if len(window)==k:
                res.append(window[-1])
                window.remove(nums[l])
                l+=1
            r+=1
        return res
