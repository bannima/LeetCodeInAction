#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/5/15 5:02 PM
@desc: 
"""


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_weight(n):
            """返回n的步数"""
            if n == 1: return 0
            return get_weight(n // 2) + 1 if n % 2 == 0 else get_weight(n * 3 + 1) + 1

        array = list(range(lo, hi + 1))
        array.sort(key=lambda x: get_weight(x))
        return array[k - 1]





