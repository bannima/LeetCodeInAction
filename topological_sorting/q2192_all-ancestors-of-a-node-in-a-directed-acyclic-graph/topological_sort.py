#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: topological_sort.py
@time: 2022/5/2 9:33 PM
@desc: 
"""
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        nexts = [[] for _ in range(n)]
        pre = [[] for _ in range(n)]
        in_degree = [0] * n
        # init adjvec
        for edge in edges:
            nexts[edge[0]].append(edge[1])
            pre[edge[1]].append(edge[0])
            in_degree[edge[1]] += 1

        # init queue
        queue = [node for node in range(n) if in_degree[node] == 0]
        res = [[] for _ in range(n)]
        # bfs
        while queue:
            node = queue.pop(0)
            for nextarc in nexts[node]:
                in_degree[nextarc] -= 1
                if in_degree[nextarc] == 0:
                    queue.append(nextarc)
                    # traverse all node's parents
                    for p in pre[nextarc]:
                        res[nextarc] += (res[p] + [p])
                    res[nextarc] = list(sorted(set(res[nextarc])))

        return res



