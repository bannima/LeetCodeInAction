#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/20 11:18 PM
Version: 0.1
"""

class Solution():
    def countPath(self,n):
        n = n+1
        dp = [[1]*n for _ in range(n)]

        for i in range(n):
            for j in range(i,n):
                if i==0:
                    dp[i][j] = dp[i][j-1]
                elif j==i:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]*2

