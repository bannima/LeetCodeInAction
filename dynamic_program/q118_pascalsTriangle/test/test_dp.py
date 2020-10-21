#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/21 12:59 PM
Version: 0.1
"""

from dynamic_program.q118_pascalsTriangle.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        numRows = 5
        res = s.generate(numRows)
        assert res ==[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]