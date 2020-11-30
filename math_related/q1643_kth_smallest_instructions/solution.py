#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/8 8:17 PM
Version: 0.1
"""


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        res = []
        v, h = destination
        for i in range(h + v):
            if h > 0:
                o = math.comb(h + v - 1, h - 1)
                if k <= o:
                    res.append('H')
                    h -= 1
                else:
                    res.append('V')
                    v -= 1
                    k -= o
            else:
                res.append('V')
                v -= 1

        return ''.join(res)