#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/20 9:03 PM
Version: 0.1
"""
class Solution(object):
    def climbStairs(self, n):
        """
        1.定义状态：
        dp[i]表示在第i层，能够走到的不同路径
        2.定义转移状态：
        dp[i] = dp[i-1]+dp[i-2]
        3.定义初始值：
        dp[1]=1

        :type n: int
        :rtype: int
        """
        dp = [1]*(n+1)
        if n==1:
            return dp[n]
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[n]