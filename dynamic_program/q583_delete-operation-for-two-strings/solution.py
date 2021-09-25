#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/9/25 9:27 AM
Version: 0.1
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def maxCommonStr(word1,word2):
            max_len = 0
            dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
            for i in range(1,len(word1)+1):
                for j in range(1,len(word2)+1):
                    if word1[i-1]==word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]+1
                        max_len = max(max_len,dp[i][j])
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return max_len
        return len(word1)+len(word2)-maxCommonStr(word1,word2)*2
