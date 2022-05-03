#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: union_find.py
@time: 2022/5/3 2:31 PM
@desc: 
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = []
        for edge in edges:
            nodes += edge
        n = len(set(nodes))
        parents = list(range(n))

        # find parent
        def find(i):
            while (parents[i] != i):
                i = parents[i]
            return i

        def union(i, j):
            parents[find(i)] = find(j)

        # merge
        for edge in edges:
            # check if edge is building a circle
            if find(edge[0] - 1) == find(edge[1] - 1):
                break
            # union i,j
            union(edge[0] - 1, edge[1] - 1)
        return edge

