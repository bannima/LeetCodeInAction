#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/20 7:54 PM
Version: 0.1
"""
from dynamic_program.q123_bestTimeToBuyAndSellStockiii.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        prices = [1,2,3,4,5]
        prices = [2,1,4]
        res = s.maxProfit(prices)
        assert res == 3