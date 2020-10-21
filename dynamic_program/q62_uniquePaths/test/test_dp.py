#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/21 1:10 PM
Version: 0.1
"""
from dynamic_program.q62_uniquePaths.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        res = s.uniquePaths(7,3)
        assert res==28