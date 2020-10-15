#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: DP_Solution.py
Description: 
Author: Barry Chow
Date: 2020/10/15 10:59 AM
Version: 0.1
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dynamic program table
        dp = [[0]*len(nums) for _ in range(len(nums))]
        max_num = nums[0]

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if j==i:
                    dp[i][j]=nums[i]
                else:
                    dp[i][j] = dp[i][j-1]+nums[j]

                if dp[i][j]>max_num:
                    max_num = dp[i][j]

        return max_num