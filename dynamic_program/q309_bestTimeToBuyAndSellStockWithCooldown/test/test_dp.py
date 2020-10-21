#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/21 10:23 AM
Version: 0.1
"""
from dynamic_program.q309_bestTimeToBuyAndSellStockWithCooldown.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        prices = [1,2,3,0,2]
        res = s.maxProfit(prices)
        assert  res == 3
