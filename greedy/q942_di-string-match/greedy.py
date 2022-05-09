#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: greedy.py
@time: 2022/5/9 2:56 PM
@desc: 
"""
from typing import List

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        array = list(range(n+1))
        print(array)
        res = []
        for c in s:
            if c=='I':
                chosen = min(array)
            else:
                chosen = max(array)
            res.append(chosen)
            array.remove(chosen)
        res += array
        return res