#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/19 8:50 PM
Version: 0.1
"""
from dynamic_program.q120_triangle.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        res = s.minimumTotal(triangle)
        assert res ==11