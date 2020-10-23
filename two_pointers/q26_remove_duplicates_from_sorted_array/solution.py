#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/23 11:21 AM
Version: 0.1
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        双指针法，i表示起始位置
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[i + 1] = nums[j]
                i = i + 1
        return i + 1

