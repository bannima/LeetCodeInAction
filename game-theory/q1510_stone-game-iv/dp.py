#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/24 11:57 PM
@desc: 
"""

import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i]表示还剩i个石子时候，当前玩家能否取胜
        self.dp = {}
        def dfs(i):
            if i not in self.dp:
                # 判断是否为 可平方的数
                if int(math.sqrt(i))**2 == i:
                    self.dp[i] = True
                else:
                    ans = True
                    for x in range(1,int(math.sqrt(i))+1):
                        ans = ans and dfs(i-x**2)
                    # 所有可能的情况，对方都取胜，只有自己认输
                    if ans:
                        self.dp[i]= False
                    else:
                        self.dp[i] = True
            return self.dp[i]

        ans = dfs(n)
        return ans


if __name__ == '__main__':
    n = 17
    ans = Solution().winnerSquareGame(n)
    print(ans)