#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/14 8:10 PM
Version: 0.1
"""
from dynamic_program.q5_longestPalindrome.dp_solution import DP_Solution
from dynamic_program.q5_longestPalindrome.center_solution import Center_Solution

class Test_Dp_Solution():
    def test_dp_center(self):
        for s,answer in zip(['babad','ac','a','bababd'],['bab','a','a','babab']):
            for solution in [DP_Solution,Center_Solution]:
                res =solution().longestPalindrome(s)
                assert res==answer




