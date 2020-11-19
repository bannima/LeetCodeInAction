#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sort.py
Description: 
Author: Barry Chow
Date: 2020/11/19 9:02 PM
Version: 0.1
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return
        nums.sort()
        nums = [0] + nums + [len(nums) + 1]
        res = []
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                res += list(range(nums[i] + 1, nums[i + 1]))

        return res
