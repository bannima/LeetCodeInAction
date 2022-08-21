#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        # init state
        dp[0][0] = True
        for j in range(1,n+1):
            if p[j-1]=='*': dp[0][j] = dp[0][j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]!='*':
                    dp[i][j] = False
                elif p[j-1]=='*':
                    # match 0,1,2+ times for *
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]
        #print(dp)
        return dp[m][n]

if __name__ == '__main__':
    s = "adceb"
    p = "*a*b"
    res = Solution().isMatch(s,p)
    print(res)