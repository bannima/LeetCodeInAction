#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/19 9:47 PM
Version: 0.1
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        imax = [nums[0]]
        imin = [nums[0]]
        for i in range(1,len(nums)):
            max_p = max(nums[i],imax[-1]*nums[i],imin[-1]*nums[i])
            imin.append(min(nums[i],imin[-1]*nums[i],imax[-1]*nums[i]))
            imax.append(max_p)
        return max(imax)