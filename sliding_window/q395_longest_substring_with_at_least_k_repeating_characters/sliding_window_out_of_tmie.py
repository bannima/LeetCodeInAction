#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window_out_of_tmie.py
Description: 
Author: Barry Chow
Date: 2021/2/27 4:47 PM
Version: 0.1
"""

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1 if k == 1 else 0

        l = r = 0
        counter = [0] * 26
        need = 0

        max_len = 0
        while (r < len(s)):
            pos = ord(s[r]) - ord('a')
            counter[pos] += 1

            if counter[pos] == 1:
                need += 1
            if counter[pos] == k:
                need -= 1

            while (l < r):
                if need == 0:
                    max_len = max(max_len, r - l + 1)
                    break
                pos = ord(s[l]) - ord('a')
                counter[pos] -= 1
                if counter[pos] == 0:
                    need -= 1
                if counter[pos] == k - 1:
                    need += 1
                l += 1
            # 返回到开始位置0
            for i in reversed(range(l)):
                pos = ord(s[i]) - ord('a')
                counter[pos] += 1
                if counter[pos] == 1:
                    need += 1
                if counter[pos] == k:
                    need -= 1

            l = 0
            r += 1
        return max_len