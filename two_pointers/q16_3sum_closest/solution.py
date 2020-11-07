#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/7 9:58 AM
Version: 0.1
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        closest = float('inf')

        for s in range(len(nums)):

            i, j = s + 1, len(nums) - 1
            while i < j:
                # save result
                total = sum([nums[s], nums[i], nums[j]])
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    while (i < j and nums[i] == nums[i + 1]): i += 1
                    i += 1
                elif total > target:
                    while (i < j and nums[j] == nums[j - 1]): j -= 1
                    j -= 1
                else:
                    return target
        return closest
