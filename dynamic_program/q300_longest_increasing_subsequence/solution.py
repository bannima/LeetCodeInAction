#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/6 3:42 PM
Version: 0.1
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        length = [1] * len(nums)
        for j in range(1, len(nums)):
            counter = 1
            for l in range(0, j):
                if nums[j] > nums[l]:
                    counter = max(length[l] + 1, counter)
            length[j] = counter

        return max(length)