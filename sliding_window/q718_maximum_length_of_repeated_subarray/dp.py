#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp.py
Description: 
Author: Barry Chow
Date: 2021/2/27 6:46 PM
Version: 0.1
"""


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # dp table
        dp = [[0] * len(A) for _ in range(len(B))]

        max_len = 0
        start = -1
        for i in range(len(A)):
            for j in range(len(B)):
                if i == 0 or j == 0:
                    if A[i] == B[j]:
                        dp[i][j] = 1
                else:
                    if A[i] == B[j]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 0
                if dp[i][j] > max_len:
                    max_len = max(max_len, dp[i][j])
                    start = i
        return max_len

