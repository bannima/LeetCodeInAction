#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/20 10:09 PM
Version: 0.1
"""
from dynamic_program.q64_minimumPathSum.dp_solution import Solution
class Test_Dp():
    def test(self):
        s = Solution()
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        res = s.minPathSum(grid)
        assert res ==7