#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/20 12:36 PM
Version: 0.1
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        def num_chars(s):
            return len(set(list(s)))

        l = 0;
        r = 0
        max_len = -1
        while (r <= len(s)):
            if num_chars(s[l:r]) <= k:
                if r - l > max_len:
                    max_len = r - l
                r += 1
            else:
                l += 1
        return max_len

