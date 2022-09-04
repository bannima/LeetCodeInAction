#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(t)+1,len(s)+1
        dp = [[0]* n for _ in range(m)]
        for i in range(1,m):
            for j in range(i,n):
                # start row
                if i==1:
                    if t[i-1]==s[j-1]:
                        dp[i][j] = dp[i][j-1]+1
                    else:
                        dp[i][j] = dp[i][j-1]
                else:
                    # calc dp[i][j]
                    if t[i-1]==s[j-1]:
                        dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i][j-1]
        return dp[-1][-1]
