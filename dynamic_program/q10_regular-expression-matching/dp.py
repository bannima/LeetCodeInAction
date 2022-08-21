#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution():
    """
     ref: https://leetcode.cn/problems/regular-expression-matching/solution/shou-hui-tu-jie-wo-tai-nan-liao-by-hyj8/
    """

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # 1. define state, dp[i][j]表示s[0:i-1]是否匹配p[0:j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 2. init state
        dp[0][0] = True  # s==None and p==None
        # s==None, dp[i][0]=False
        # p==None, if p[j-1]==*,dp[0][j]= dp[0][j-2] else False
        for j in range(2, n + 1):
            dp[0][j] = dp[0][j - 2] if p[j - 1] == '*' else False
        # 3. traverse dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # s[i-1]!=p[j-1]
                elif p[j - 1] != '*':
                    dp[i][j] = False
                # p[j-1]=='*'
                elif s[i - 1] == p[j - 2] or p[j - 2] == '.':
                    # * match 0 times, 1 times, 2+times
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                # s[i-1]!=p[j-2]
                elif s[i - 1] != p[j - 2]:
                    dp[i][j] = dp[i][j - 2]
        #print(dp)
        return dp[m][n]


if __name__ == '__main__':
    s = "aab"
    p = "c*a*b"
    res = Solution().isMatch(s,p)
    print(res)