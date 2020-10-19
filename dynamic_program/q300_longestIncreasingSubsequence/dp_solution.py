#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/19 7:23 PM
Version: 0.1
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        # dynamic program table
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)