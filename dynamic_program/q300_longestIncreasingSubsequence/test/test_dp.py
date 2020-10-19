#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/19 7:25 PM
Version: 0.1
"""

from dynamic_program.q300_longestIncreasingSubsequence.dp_solution import Solution


class Test_Dp():
    def test_dp(self):
        s = Solution()
        nums = [1,3,6,7,9,4,10,5,6]
        res = s.lengthOfLIS(nums)
        assert res ==6
