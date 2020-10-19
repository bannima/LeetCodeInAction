#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/19 9:48 PM
Version: 0.1
"""
from dynamic_program.q152_maximumProductSubarray.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        nums = [-4,-3,-2]
        res = s.maxProduct(nums)
        assert res==12