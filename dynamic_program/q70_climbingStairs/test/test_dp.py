#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/20 9:03 PM
Version: 0.1
"""
from dynamic_program.q70_climbingStairs.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        res = s.climbStairs(4)
        assert res==5