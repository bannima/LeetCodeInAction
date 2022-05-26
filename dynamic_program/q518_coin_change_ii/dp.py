#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/27 12:22 AM
@desc: 
"""
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {}

        def dfs(i, j):
            if (i, j) not in dp:
                """使用前i种硬币（含i,i从0开始计算），得到和为j的组合数"""
                if j<0:
                    ans = 0
                elif j==0:
                    ans = 1
                else:
                    ans = 0
                    for s in range(i + 1):
                        ans += dfs(s, j - coins[s])

                dp[(i, j)] = ans
            return dp[(i, j)]

        ans = dfs(len(coins) - 1, amount)
        print(dp)
        return ans

if __name__ == '__main__':
    amount = 5
    coins = [1,2,5]
    ans = Solution().change(amount,coins)
    print(ans)
