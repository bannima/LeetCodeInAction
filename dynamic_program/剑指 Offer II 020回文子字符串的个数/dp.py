#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/26 10:42 PM
@desc: 
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        ans = n
        for l in range(1, n):
            for i in range(n - l):
                j = i + l
                if l == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j]:
                    ans += 1

        return ans
if __name__ == "__main__":
    s = "aaab"
    ans = Solution().countSubstrings(s)
    print(ans)
