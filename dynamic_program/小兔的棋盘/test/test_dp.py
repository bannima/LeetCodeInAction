#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/20 11:21 PM
Version: 0.1
"""
from dynamic_program.小兔的棋盘.dp_solution import Solution

class Test_Dp():
    def test(self):
        ns = [1,3,12]
        answers = [2,10,416024]
        for n,ans in zip(ns,answers):
            res = Solution().countPath(n)
            assert res==ans