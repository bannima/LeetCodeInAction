#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: force.py
Description: 
Author: Barry Chow
Date: 2021/2/20 10:58 AM
Version: 0.1
"""

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < k and nums[i] + nums[j] > sum:
                    sum = nums[i] + nums[j]
        return sum
