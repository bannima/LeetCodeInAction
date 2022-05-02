#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: topological_sort.py
@time: 2022/5/2 10:00 PM
@desc: 
"""
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return list(range(n))
        nextarcs = [[] for _ in range(n)]
        in_degrees = [0] * n
        # init nextarcs
        for edge in edges:
            in_degrees[edge[0]] += 1
            in_degrees[edge[1]] += 1
            nextarcs[edge[0]].append(edge[1])
            nextarcs[edge[1]].append(edge[0])
        # init queue
        queue = [node for node in range(n) if in_degrees[node] == 1]
        visited = [-1] * n
        for node in queue:
            visited[node] = 0

        while sum(visited):
            next_queue = []
            for node in queue:
                for nextarc in nextarcs[node]:
                    in_degrees[nextarc] -= 1
                    if in_degrees[nextarc] == 1:
                        next_queue.append(nextarc)
                        visited[nextarc] = 0
            queue = next_queue

        return queue


