#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word2), len(word1)
        # step 1.定义状态：dp[i][j] 表示将 word1[0:i]编辑到word2[0:j]上所需要的最小操作数
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # step 2.初始化dp值
        # 相当于从空字符开始，不断删除字符，使得等于word2
        for i in range(m + 1): dp[i][0] = i
        # 相当于从空字符串开始，不断插入字符，使得等于word1
        for j in range(n + 1): dp[0][j] = j

        # step3: 定义自底向上dp的遍历方向
        for i in range(1, m + 1):  # 遍历word2的每一行
            for j in range(1, n + 1):  # 遍历word1的每一列
                # step 4: 定义状态转移方程
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # 相等，
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # 删除word2的字符
                        dp[i][j - 1] + 1,  # 插入word1的字符
                        dp[i - 1][j - 1] + 1  # 替换字符
                    )
        return dp[-1][-1]