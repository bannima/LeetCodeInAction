#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: two_pointer.py
@time: 2022/5/13 9:44 PM
@desc: 
"""

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        n,m = len(first),len(second)
        if n>m:
            return self.oneEditAway(second,first)
        if m-n>=2:return False
        l,r,ops = 0,0,0
        while(l<n and r<m and ops<=2):
            if first[l]!=second[r]:
                ops+=1
                if m==n:
                    l+=1
                    r+=1
                else:
                    r+=1
            else:
                l+=1
                r+=1
        return ops<=1