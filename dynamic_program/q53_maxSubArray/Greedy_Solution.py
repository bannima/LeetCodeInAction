#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: Greedy_Solution.py
Description: 
Author: Barry Chow
Date: 2020/10/15 11:49 AM
Version: 0.1
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        before_max = 0
        cur_max = total_max = nums[0]
        for i in range(0,len(nums)):
            if before_max <0:
                cur_max = nums[i]
            else:
                cur_max = before_max+nums[i]

            before_max = cur_max
            if cur_max>total_max:
                total_max = cur_max

        return total_max