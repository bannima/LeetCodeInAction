#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/1 8:48 PM
Version: 0.1
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)
        pos = -1
        while (i < j):
            if nums[(i + j) // 2] == target:
                pos = (i + j) // 2
                break
            elif nums[(i + j) // 2] > target:
                j = (i + j) // 2
            else:
                i = (i + j + 1) // 2
        i = pos;
        j = pos
        if pos != -1:
            while ((i - 1) >= 0 and nums[i - 1] == target): i -= 1
            while ((j + 1) < len(nums) and nums[j + 1] == target): j += 1
        return [i, j]

