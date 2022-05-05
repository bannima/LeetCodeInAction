#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: sliding_window.py
@time: 2022/5/6 12:07 AM
@desc: 
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = [0]*128
        l = 0
        max_l = -1
        def is_duplicate(counter):
            for v in counter:
                if v>1:
                    return True
            return False
        for r,v in enumerate(list(s)):
            counter[ord(v)-97]+=1
            while is_duplicate(counter):
                counter[ord(s[l])-97]-=1
                l += 1
            max_l = max(max_l,r-l+1)
        return max_l

if __name__ == '__main__':
    s = "abcabcbb"
    res = Solution().lengthOfLongestSubstring(s)
    print(res)