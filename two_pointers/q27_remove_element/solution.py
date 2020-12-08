#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/8 11:25 AM
Version: 0.1
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while (j < len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

