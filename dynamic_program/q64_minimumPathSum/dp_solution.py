#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/20 10:07 PM
Version: 0.1
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        dp[i][j]表示在(i,j)位置的最小路径

        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]

        if m == 1 and n == 1:
            return grid[0][0]

        dp[0][0] = grid[0][0]
        for i in range(0, m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                    continue
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
