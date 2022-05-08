#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: sliding_window.py
@time: 2022/5/8 9:57 PM
@desc: 
"""
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        定长滑动窗口
        """
        k = sum(nums)
        # for circle
        nums = nums+nums
        max_ones = sum(nums[:k])
        cur_ones = sum(nums[:k])
        for r in range(k,len(nums)):
            #legal r
            cur_ones += nums[r]
            cur_ones -= nums[r-k]
            max_ones = max(max_ones,cur_ones)

        return k-max_ones
