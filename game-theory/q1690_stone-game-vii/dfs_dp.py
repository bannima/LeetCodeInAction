#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs_dp.py
@time: 2022/5/25 7:41 PM
@desc: 超时

"""
from typing import List

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        self.dp = {}

        pre_sum = []
        cur_sum = 0
        for i in range(len(stones)):
            cur_sum += stones[i]
            pre_sum.append(cur_sum)

        def dfs(l, r):
            if (l, r) not in self.dp:
                if l == r or l + 1 == r:
                    max_gain = 0
                else:
                    totols_sum = pre_sum[r - 1] - pre_sum[l] + stones[l]
                    max_gain = totols_sum - stones[l] - dfs(l + 1, r)
                    max_gain = max(max_gain, totols_sum - stones[r - 1] - dfs(l, r - 1))
                self.dp[(l, r)] = max_gain
            return self.dp[(l, r)]

        ans = dfs(0, len(stones))
        return ans
