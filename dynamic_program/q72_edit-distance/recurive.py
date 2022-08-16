#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # memory 递归，自顶向下
        @lru_cache
        def min_op(i, j):
            # 表示word1[:i]到word2[:j]所需要的最小操作次数
            if i == 0 or j == 0:
                return i + j  # dp[i][0] = i,dp[0][j] = j
            if word2[i - 1] == word1[j - 1]:
                return min_op(i - 1, j - 1)
            return min(min_op(i - 1, j), min_op(i - 1, j - 1), min_op(i, j - 1)) + 1

        return min_op(len(word2), len(word1))
