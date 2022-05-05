#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: sliding_window.py
@time: 2022/5/5 8:02 PM
@desc: 
"""

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        counter = {}
        res = []

        def distinct_char(counter):
            for key, val in counter.items():
                if val > 1:
                    return False
            return True

        def add(c):
            if c not in counter:
                counter[c] = 0
            counter[c] += 1

        def remove(c):
            counter[c] -= 1

        for r, c in enumerate(list(s)):
            #print(r, c)
            if r < 2:
                add(c)
                continue
            add(c)
            while r - l > 2:
                remove(s[l])
                l += 1
            if distinct_char(counter):
                res.append(s[l:r + 1])
        return len(res)

if __name__ =='__main__':
    s = "xyzzaz"
    s = "aababcabc"
    res = Solution().countGoodSubstrings(s)
    print(res)

