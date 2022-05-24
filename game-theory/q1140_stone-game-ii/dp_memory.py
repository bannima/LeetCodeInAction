#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp_memory.py
@time: 2022/5/24 10:08 PM
@desc: 
"""

from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        self.dp = {}

        def dfs(i, M):
            """
            表示从第i堆石子开始（含第i堆），以M为范围，在[1,2*M]范围内，
            拿取x堆石子后能够得到的最大石子数量
            """
            if (i, M) not in self.dp:
                # 剩余石子数量为0
                if i >= n:
                    ans = 0
                # 能够拿到剩下的所有石子
                elif 2 * M + i >= n:
                    ans = sum(piles[i:])
                # 从[1,2*M]中递归遍历得到最优解
                else:
                    ans = float("-inf")
                    # x表示我拿了多少石子
                    for x in range(1, 2 * M + 1):
                        ans = max(ans, sum(piles[i:]) - dfs(i + x, max(x, M)))
                self.dp[(i, M)] = ans
            return self.dp[(i, M)]

        return dfs(0, 1)



