#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/20 5:09 PM
Version: 0.1
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        max_len = 0
        n = [0] * 26
        while (r < len(s)):
            n[ord(s[r]) - ord('A')] += 1
            r += 1
            while r - l - max(n) > k:
                n[ord(s[l]) - ord('A')] -= 1
                l += 1

            if r - l > max_len:
                max_len = r - l

        return max_len




