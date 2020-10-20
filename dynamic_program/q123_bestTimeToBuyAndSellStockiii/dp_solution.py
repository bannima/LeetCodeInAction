#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/20 7:54 PM
Version: 0.1
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dynamic table
        dp = [[0] * 3 for _ in range(2)]
        # inital value
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        # 1次和2次售出股票在第0步是不可能的
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf')
        dp[1][1] = float('-inf')
        dp[1][2] = float('-inf')

        for i in range(1, len(prices)):
            # 转移方程

            dp_0_0 = dp[0][0]
            dp_0_1 = max(dp[0][1], dp[1][0] + prices[i])
            dp_0_2 = max(dp[0][2], dp[1][1] + prices[i])

            dp_1_0 = max(dp[1][0], dp[0][0] - prices[i])
            dp_1_1 = max(dp[1][1], dp[0][1] - prices[i])
            dp_1_2 = max(dp[1][2], dp[0][2] - prices[i])

            dp[0][0] = dp_0_0
            dp[0][1] = dp_0_1
            dp[0][2] = dp_0_2

            dp[1][0] = dp_1_0
            dp[1][1] = dp_1_1
            dp[1][2] = dp_1_2

        return max(dp[0])