#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: union_find.py
@time: 2022/5/3 11:15 AM
@desc: 并查集
"""
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parents = list(range(n))

        # union operation
        def union(i, j):
            parents[find(i)] = find(j)

        # find parent operation
        def find(i):
            while parents[i] != i:
                i = parents[i]
            return i
        # find and union
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]==1:
                    union(i,j)
        # calc province nums
        return len(set([find(i) for i in range(n)]))

if __name__ == '__main__':
    isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    res = Solution().findCircleNum(isConnected)
    print(res)

