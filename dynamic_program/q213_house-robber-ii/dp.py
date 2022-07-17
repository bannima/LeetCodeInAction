#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/7/17 11:37 AM
@desc: 
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        #把环破解成两个队列 [0:n-1],[1:n], 取最大值
        def rob_with_nums(nums):
            n = len(nums)
            dp = [0]*(n+1)
            dp[1] = nums[0]
            for i in range(1,n):
                dp[i+1] = max(dp[i-1]+nums[i],dp[i])
            return dp[-1]

        if len(nums)==1:
            return nums[0]
        return max(rob_with_nums(nums[1:]),rob_with_nums(nums[:len(nums)-1]))



