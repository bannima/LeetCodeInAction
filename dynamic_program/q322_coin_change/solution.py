#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/18 4:31 PM
Version: 0.1
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        if len(coins) == 1:
            return -1 if amount % coins[0] != 0 else int(amount / coins[0])

        # dynamic programing
        F = [0] * (amount + 1)
        for s in range(1, amount + 1):
            tmp = []
            for c in coins:
                if s - c >= 0:
                    tmp.append(F[s - c])
            F[s] = min(tmp) + 1 if len(tmp) > 0 else float('inf')
        return F[-1] if F[-1] != float('inf') else -1
