#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_greedy.py
Description: 
Author: Barry Chow
Date: 2020/10/15 11:49 AM
Version: 0.1
"""
from dynamic_program.q53_maxSubArray.Greedy_Solution import Solution
class Test_Greedy():
    def test_greedy(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4, 10, 21, -32, 12, 2, 32, 1, 2]
        res = Solution().maxSubArray(nums)
        assert res == 53