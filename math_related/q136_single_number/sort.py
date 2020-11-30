#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sort.py
Description: 
Author: Barry Chow
Date: 2020/11/19 8:35 PM
Version: 0.1
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums.sort()
        i = 0
        while (i < len(nums) - 1):
            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
        return nums[len(nums) - 1]
