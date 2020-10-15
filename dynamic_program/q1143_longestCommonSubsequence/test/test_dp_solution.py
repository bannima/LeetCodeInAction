#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/15 10:20 AM
Version: 0.1
"""
from dynamic_program.q1143_longestCommonSubsequence import Solution
class Test_DP_Solution():
    def test_dp(self):
        text1 = 'algorithms'
        text2 = 'alchemist'
        common_subsequence = Solution().longestCommonSubsequence(text1,text2)
        assert common_subsequence==5
