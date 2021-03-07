#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp.py
Description: 
Author: Barry Chow
Date: 2021/3/7 4:15 PM
Version: 0.1
"""


class Solution:
    def minCut(self, s: str) -> int:
        # palid[i][j]表示s[i,..,j+1]是否为回文串
        palid = [[True] * len(s) for _ in range(len(s))]

        for l in range(1, len(s)):
            for i in range(len(s) - l):
                if l == 1:
                    palid[i][i + l] = s[i] == s[i + l]
                else:
                    palid[i][i + l] = (s[i] == s[i + l]) and palid[i + 1][i + l - 1]

        # dp[i]表示s[:i+1]的最小分割次数
        dp = [0] * len(s)

        for i in range(len(s)):
            min_t = float('inf')
            # 若s[:i+1]是回文串，则分割次数为0
            if palid[0][i]:
                dp[i] = 0
            # 若不是，则依次取中间位置j，若s[j+1:i+1]是回文串，
            # 则dp[i+1] = min(dp[j]+1) if palid[j+1][i+1]==True
            # for all j in range(0,i).
            else:
                for j in range(i):
                    if palid[j + 1][i]:
                        min_t = min(min_t, dp[j] + 1)
                        dp[i] = min_t

        return dp[-1]
