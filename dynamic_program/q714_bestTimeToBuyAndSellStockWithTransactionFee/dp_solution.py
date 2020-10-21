#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/21 10:42 AM
Version: 0.1
"""
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        dp[i][0]:第i天持有现金的最大收益
        dp[i][1]：第i天持有股票的最大收益
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        #边界值
        if len(prices)==0:
            return 0
        #dp table
        dp = [[0]*2 for i in range(len(prices))]
        #初始值
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        #状态转移
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]