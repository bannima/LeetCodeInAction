
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/25 7:41 PM
@desc: 
"""

from typing import List

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0]* n for _ in range(n)]
        #
        pre_sum = []
        cur_sum = 0
        for i in range(n):
            cur_sum+=stones[i]
            pre_sum.append(cur_sum)

        #dp[l][r]表示给定数组[l,r-1]可以得到的最大分差

        for s in range(1,n):
            for l in reversed(range(n-s)):
                #(l,r) = [i,i+s]
                r = l+s
                total_s = pre_sum[r] - pre_sum[l] + stones[l]
                dp[l][r] = max(total_s - stones[l] - dp[l+1][r],total_s - stones[r] -dp[l][r-1])
        #print(dp)
        return dp[0][n-1]


if __name__ == '__main__':
    stones = [5, 3, 1, 4, 2]
    ans = Solution().stoneGameVII(stones)
    print(ans)