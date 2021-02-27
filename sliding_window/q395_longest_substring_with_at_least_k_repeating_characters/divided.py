#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: divided.py
Description: 
Author: Barry Chow
Date: 2021/2/27 5:23 PM
Version: 0.1
"""
from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def dfs(s, l, r, k):
            # 找到区间s[l:r+1]内包含最长串的最大值
            counter = Counter(s[l:r + 1])
            split_chars = []
            for c, time in counter.items():
                if time < k:
                    split_chars.append(c)
            if len(split_chars) == 0:
                return r - l + 1

            splits = []
            for i in range(l, r + 1):
                if s[i] in split_chars:
                    splits.append(i)

            max_len = 0
            start = l
            for i in splits:
                end = i - 1
                max_len = max(max_len, dfs(s, start, end, k))

                start = i + 1
            max_len = max(max_len, dfs(s, start, r, k))
            return max_len

        return dfs(s, 0, len(s) - 1, k)