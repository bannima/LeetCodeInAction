#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/20 12:43 PM
Version: 0.1
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        状态定义：
            dp[i][0]表示到i步时，持有现金所获得的最大收益
            dp[i][1]表示到i步时，持有股票所获得的最大收益
        状态转移方程:
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        即第i步时，持有现金的最大收益，可以从上一步持有股票卖出到现金，
        或者继续持有现金转移，两种情况比较最大值得来
        :type prices: List[int]
        :rtype: int
        """
        # dynamic table
        dp = [[0] * 2 for _ in range(len(prices))]
        # initial value
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[-1][0]