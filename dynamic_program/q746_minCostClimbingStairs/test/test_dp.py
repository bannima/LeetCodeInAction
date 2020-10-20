#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/20 9:34 PM
Version: 0.1
"""

from dynamic_program.q746_minCostClimbingStairs.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        cost = [0,0,0,0]
        res = s.minCostClimbingStairs(cost)
        assert res==0