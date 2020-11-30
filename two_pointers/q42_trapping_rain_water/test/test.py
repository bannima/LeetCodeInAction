#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/23 8:58 PM
Version: 0.1
"""
from two_pointers.q42_trapping_rain_water.stack_solution import Solution

class Test():
    def test(self):
        s = Solution()
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        res = s.trap(height)
        assert res ==6

    def test2(self):
        s = Solution()
        height = [4,2,0,3,2,5]
        res = s.trap(height)
        assert res == 9