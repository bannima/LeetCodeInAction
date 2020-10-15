#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/15 10:59 AM
Version: 0.1
"""
from dynamic_program.q53_maxSubArray.DP_Solution import Solution
class Test_DP():
    def test_dp(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 10, 21, -32, 12, 2, 32, 1, 2]
        res = Solution().maxSubArray(nums)
        assert res == 53