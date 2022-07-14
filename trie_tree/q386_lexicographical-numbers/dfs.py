#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/7/14 9:22 PM
@desc: 
"""
from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(m):
            if m>n: return
            res.append(m)
            for i in range(10): dfs(m*10 +i)
        for i in range(1,10): dfs(i)
        return res

