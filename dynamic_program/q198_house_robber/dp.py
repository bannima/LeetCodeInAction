#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp.py
Description: 
Author: Barry Chow
Date: 2020/11/20 8:31 PM
Version: 0.1
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        关键在于状态转移方程
        dp[i]表示在i时，所能取得的最大现金
        所以：
        dp[i] = max(dp[i-1],dp[i-2]+nums[i],dp[i-3]+nums[i],dp[i-4]+nums[i]+...+dp[0]+nums[i])
        注意，dp[i-4]+nums[i],dp[i-5]+nums[i],...,dp[0]+nums[i]<= dp[i-2]+nums[i]
        因为从0,...,i-4 中的任意一步到i-2步，可以任意选择增加一次偷窃，所以dp[i-2]肯定比dp[i-4],dp[i-5],...等值大
        所以可以简化为：
        dp[i] = max(dp[i-1],dp[i-2]+nums[i],dp[i-3]+nums[i])
        '''
        if len(nums)<=1:
            return nums[0] if len(nums)==1 else 0
        #dynamic programing
        dp = [0]*len(nums)

        #inital value
        dp[0] = nums[0]
        dp[1] = nums[1]

        #state transform
        for i in range(2,len(nums)):
            dp[i]= max(dp[i-1],dp[i-2]+nums[i],dp[i-3]+nums[i])

        return max(dp[-1],dp[-2])