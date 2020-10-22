#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/22 9:30 AM
Version: 0.1
"""


class Dp_Solution(object):
    def wordBreak(self, s, wordDict):
        """
        dp[i]表示s[0:i]是否可以拆分

        dp[i+l]=dp[i-1] and s[i:i+l] in wordDict

        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        lengths = set([len(word) for word in wordDict])

        dp = [False] * len(s)

        for i in range(len(s)):
            for l in lengths:
                if (i + l - 1) < len(s):
                    if i == 0:
                        tmp = s[i:i + l] in wordDict
                    else:
                        tmp = dp[i - 1] and (s[i:i + l] in wordDict)
                    dp[i + l - 1] = dp[i + l - 1] or tmp

        return dp[-1]
