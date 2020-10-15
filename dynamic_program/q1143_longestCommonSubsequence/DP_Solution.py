#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: DP_Solution.py
Description: 
Author: Barry Chow
Date: 2020/10/15 10:19 AM
Version: 0.1
"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        动态规划法解决最长公共子序列
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #dynamic program table
        dp = [[0]*(len(text2)+1) for _ in range(1+len(text1))]
        max_length = 0
        for i in range(1,1+len(text1)):
            for j in range(1,1+len(text2)):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    if dp[i][j]>max_length:
                        max_length = dp[i][j]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return max_length