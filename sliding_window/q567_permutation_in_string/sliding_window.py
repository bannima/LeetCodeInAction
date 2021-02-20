#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/20 6:00 PM
Version: 0.1
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def equals(a,b):
            for key in a.keys():
                if a[key]!=b[key]:
                    return False
            return True

        n1 = len(s1)
        c1 = Counter(s1)
        n2 = len(s2)
        c2 = Counter()

        l = r = 0
        while r<len(s2):
            if s2[r] not in c1:
                l = r+1
                c2.clear()
            else:
                c2.update(s2[r])
                if c2[s2[r]]>c1[s2[r]]:
                    while(s2[l]!=s2[r]):
                        c2[s2[l]]-=1
                        l+=1
                    c2[s2[l]]-=1
                    l+=1
                else:
                    if equals(c1,c2):
                        return True
            r+=1
        return False