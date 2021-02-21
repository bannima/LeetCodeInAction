#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window_sortedlist.py
Description: 
Author: Barry Chow
Date: 2021/2/21 10:59 AM
Version: 0.1
"""

from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = SortedList()

        l = r = 0
        max_len = 0

        while (r < len(nums)):
            window.add(nums[r])
            while window[-1] - window[0] > limit:
                window.remove(nums[l])
                l += 1

            max_len = max(max_len, r - l + 1)

            r += 1

        return max_len