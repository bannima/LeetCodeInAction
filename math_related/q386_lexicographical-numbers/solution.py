#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/4/18 7:19 PM
@desc: 
"""

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(cur,n):
            if cur>n: return
            res.append(cur)
            for i in range(0,10):dfs(10*cur + i,n)
        for i in range(1,10):dfs(i,n)
        return res