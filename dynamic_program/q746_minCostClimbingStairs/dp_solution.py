#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/20 9:34 PM
Version: 0.1
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        1.定义状态：
        dp[i]表示到第i层，最小的花费
        2.定义状态转移方程
        dp[i]= min(dp[i-1],dp[i-2])+cost[i]
        3.边界值
        dp[0]=cost[0]
        dp[1] = cost[1]
        注意cost中没有最后到达终点的为0的cost，append 0

        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        dp = [0] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return dp[-1]
