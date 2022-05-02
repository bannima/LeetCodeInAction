#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: topological_sort_hierarchical_traverse.py
@time: 2022/5/2 8:17 PM
@desc: 
"""

from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adjvec = [[] for _ in range(n)]
        pre = [[] for _ in range(n)]
        in_degree = [0] * n
        # init adjvec
        for relation in relations:
            adjvec[relation[0]-1].append(relation[1]-1)
            in_degree[relation[1]-1] +=1
            pre[relation[1]-1].append(relation[0]-1)
        # init queue
        queue = [node for node in range(n) if in_degree[node]==0]
        # bfs
        min_month = [0] * n
        for node in queue:
            min_month[node] = time[node]
        while queue:
            # bfs
            node = queue.pop(0)
            for nextarc in adjvec[node]:
                in_degree[nextarc]-=1
                #  0 indegree
                if in_degree[nextarc]==0:
                    queue.append(nextarc)
                    # calc node's min month with dp
                    min_month[nextarc] = max([min_month[p] for p in pre[nextarc]]) + time[nextarc]
        print(min_month)
        return max(min_month)

if __name__ == '__main__':
    n = 9
    relations = [[2, 7], [2, 6], [3, 6], [4, 6], [7, 6], [2, 1], [3, 1], [4, 1], [6, 1], [7, 1], [3, 8], [5, 8], [7, 8], [1, 9],
     [2, 9], [6, 9], [7, 9]]
    time = [9, 5, 9, 5, 8, 7, 7, 8, 4]
    res = Solution().minimumTime(n=n,relations=relations,time=time)
    print(res)