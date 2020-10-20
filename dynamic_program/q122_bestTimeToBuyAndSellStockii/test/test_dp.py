#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/20 12:43 PM
Version: 0.1
"""
from dynamic_program.q122_bestTimeToBuyAndSellStockii.dp_solution import Solution
class Test_Dp():
    def test(self):
        s = Solution()
        prices = [7,1,5,3,6,4]
        res = s.maxProfit(prices)
        assert res==7