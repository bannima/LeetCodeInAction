#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/24 10:51 PM
@desc: 
"""
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        self.dp = {}

        def dfs(i,M):
            """
            表示从第i堆石子开始，选择m堆[1,2,3]石子，可以得到的最大石子的 差值
            """
            if (i,M) not in self.dp:
                #
                if i>=n:
                    ans = 0
                elif i+M>=n:
                    ans = sum(stoneValue[i:])
                else:
                    oppo = float("-inf")
                    # 遍历三种可能1,2,3
                    for x in range(1,3+1):
                        # 遍历三种可能 对手获得的最大值
                        oppo = max(oppo,dfs(i+M,x))
                    ans = sum(stoneValue[i:i+M])-oppo
                self.dp[(i,M)] = ans
            return self.dp[(i,M)]

        max_v = float("-inf")
        for i in range(1,3+1):
            max_v = max(max_v,dfs(0,i))
        #print(max_v)
        if max_v>0:
            return "Alice"
        elif max_v==0:
            return "Tie"
        return "Bob"

if __name__ == '__main__':
    stoneValue = [1, 2, 3, 7]
    ans = Solution().stoneGameIII(stoneValue)
    print(ans)

