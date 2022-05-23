#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/23 7:04 PM
@desc: 
"""
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[i][j]表示 nums[i:j]数组中选择任意策略，能让当前选择人，获得的收益的最大值
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        #注意遍历方向，l表示window size，i表示起始位置
        for l in range(1,n):
            for i in range(0,n-l)[::-1]:
                j = i+l
                # 两种策略，选择头或者尾元素，则收益为 当前元素减去对手选择区间的最大收益
                dp[i][j] = max(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])
        return dp[0][n-1]>0
