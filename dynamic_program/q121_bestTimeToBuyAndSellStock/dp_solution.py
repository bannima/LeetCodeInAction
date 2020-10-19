#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/19 10:52 PM
Version: 0.1
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > min_price:
                if (prices[i] - min_price) > max_profit:
                    max_profit = prices[i] - min_price
            else:
                min_price = prices[i]

        return max_profit
