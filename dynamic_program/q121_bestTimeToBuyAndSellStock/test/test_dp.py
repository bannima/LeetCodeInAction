#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/19 10:52 PM
Version: 0.1
"""
from dynamic_program.q121_bestTimeToBuyAndSellStock.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        prices = [7,1,5,3,6,4]
        res = s.maxProfit(prices)
        assert res == 5