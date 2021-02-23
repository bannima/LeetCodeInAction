#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/23 7:49 PM
Version: 0.1
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = 0
        r = 0
        s = sum(nums)
        target = s - x

        window = 0
        max_len = -1
        while (r < len(nums)):
            window += nums[r]

            if window > target:
                while (window > target and l <= r):
                    window -= nums[l]
                    l += 1

            if window == target:
                max_len = max(max_len, r - l + 1)
            r += 1
        return len(nums) - max_len if max_len != -1 else max_len





