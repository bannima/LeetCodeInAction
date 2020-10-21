#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/21 10:23 AM
Version: 0.1
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        1.定义状态
        dp[i][0]:表示在i天，持有现金的最大利润，此时第二天可以进行股票交易
        dp[i][1]:表示在i天，持有股票的最大利润
        dp[i][2]:表示在i天，进入冷冻期的最大利润，此时第二天不可以进行股票交易

        2.定义转移方程
        #持有现金的收益由前一天持有现金或者结束冷冻期最大值
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
        #持有股票最大收益由前一天持有股票收益或买入股票最大收益获得
        dp[i][1] = max(dp[i - 1][1],  dp[i - 1][0] - prices[i])
        #进入冷冻期最大收益只有前一天卖出股票所得
        dp[i][2] = dp[i - 1][1] + prices[i]
        
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0] * 3 for _ in range(len(prices))]
        # inital value
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = float('-inf')

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            dp[i][1] = max(dp[i - 1][1],  dp[i - 1][0] - prices[i])
            dp[i][2] = dp[i - 1][1] + prices[i]

        return max(dp[-1][0],dp[-1][2])