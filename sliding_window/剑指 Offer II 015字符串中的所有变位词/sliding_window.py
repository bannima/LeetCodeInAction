#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: sliding_window.py
@time: 2022/5/5 8:25 PM
@desc: 
"""
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = [0]*27
        for pc in p:
            counter_p[ord(pc)-97]+=1
        counter_s = [0]*27
        l = 0
        res = []
        def is_same(countera,counterb):
            for i in range(27):
                if countera[i]!=counterb[i]:
                    return False
            return True

        for r,c in enumerate(list(s)):
            if r<len(p)-1:
                counter_s[ord(c)-97]+=1
                continue
            counter_s[ord(c) - 97] += 1
            if r-l>=len(p):
                counter_s[ord(s[l])-97]-=1
                l+=1
            # check eval
            if is_same(counter_p,counter_s):
                res.append(l)
        return res

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    res = Solution().findAnagrams(s,p)
    print(res)