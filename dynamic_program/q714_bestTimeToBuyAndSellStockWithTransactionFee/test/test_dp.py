#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/21 10:42 AM
Version: 0.1
"""
from dynamic_program.q714_bestTimeToBuyAndSellStockWithTransactionFee.dp_solution import Solution
class Test_Dp():
    def test(self):
        s = Solution()
        prices = [1,3,2,8,4,9]
        fee = 2
        res = s.maxProfit(prices,fee)
        assert  res == 8