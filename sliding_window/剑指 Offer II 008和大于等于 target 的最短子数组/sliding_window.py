#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: sliding_window.py
@time: 2022/5/9 8:11 PM
@desc: 
"""
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,cur_sum = 0,0
        min_len = float("inf")
        for r,v in enumerate(nums):
            cur_sum+=v
            while cur_sum>=target:
                min_len = min(min_len,r-l+1)
                cur_sum -= nums[l]
                l+=1
        return min_len if min_len!=float("inf") else 0