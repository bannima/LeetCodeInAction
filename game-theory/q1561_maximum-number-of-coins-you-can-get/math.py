#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: math.py
@time: 2022/5/23 8:54 PM
@desc: 
"""
from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)//3
        s = 0
        for i in range(n,3*n,2):
            s += piles[i]
        return s

