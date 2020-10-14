#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 回文子串的动态规划解法
参考题解：动态规划、中心扩散、Manacher 算法(https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/)
Author: Barry Chow
Date: 2020/10/14 7:30 PM
Version: 0.1
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        dynamic progarm method
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s
        # dynamic program table
        dp = [[True] * length for _ in range(length)]

        max_length = 0
        start_position = 0
        # count table
        for r in range(1, length):
            for l in range(r):
                if (r - l) == 1:
                    dp[l][r] = s[l] == s[r]
                else:
                    dp[l][r] = (s[l] == s[r]) and dp[l + 1][r - 1]

                # if true, save max length and start position
                if dp[l][r]:
                    if (r - l) > max_length:
                        max_length = r - l
                        start_position = l

        return s[start_position:start_position + max_length+1]
