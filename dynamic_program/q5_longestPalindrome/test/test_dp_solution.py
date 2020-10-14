#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/14 8:10 PM
Version: 0.1
"""
from dynamic_program.q5_longestPalindrome.dp_solution import Solution
class Test_Dp_Solution():
    def test_dp(self):
        for s,answer in zip(['babad','ac','a','bababd'],['bab','a','a','babab']):
            res = Solution().longestPalindrome(s)
            assert res==answer



