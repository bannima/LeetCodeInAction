#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/25 3:29 PM
Version: 0.1
"""

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [nums[0]]+[0]*(len(nums)-1)
        for j in range(1,len(nums)):
            arr[j] = nums[j] +arr[j-1]
        return arr