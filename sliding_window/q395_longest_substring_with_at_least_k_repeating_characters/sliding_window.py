#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/27 3:31 PM
Version: 0.1
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        max_len = 0
        for t in range(1, 26 + 1):
            l = r = 0
            need = 0
            counter = [0] * 26
            total = 0

            while (r < len(s)):
                # update s[r]
                pos = ord(s[r]) - ord('a')
                counter[pos] += 1

                # update need,max_len
                if counter[pos] == 1:
                    total += 1
                    need += 1
                if counter[pos] == k:
                    need -= 1

                while (total > t):
                    pos = ord(s[l]) - ord('a')
                    counter[pos] -= 1

                    if counter[pos] == k - 1:
                        need += 1

                    if counter[pos] == 0:
                        need -= 1
                        total -= 1
                    l += 1
                if need == 0:
                    max_len = max(max_len, r - l + 1)
                r += 1
        return max_len
