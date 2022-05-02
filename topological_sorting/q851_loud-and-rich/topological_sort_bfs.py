#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: topological_sort_bfs.py
@time: 2022/5/2 4:37 PM
@desc: 
"""

from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        numPersons = len(quiet)
        adjvec = [[] for _ in range(numPersons)]
        in_degree = [0] * numPersons
        # init adjvec
        for pair in richer:
            adjvec[pair[0]].append(pair[1])
            in_degree[pair[1]] += 1
        # init queue
        queue = [node for node in range(numPersons) if in_degree[node] == 0]

        # get the min quiet person in queue
        res = list(range(numPersons))
        for node in queue:
            res[node] = node

        while queue:
            node = queue.pop(0)

            for nextarc in adjvec[node]:
                # update the min quiet person
                if quiet[res[node]] < quiet[res[nextarc]]:
                    res[nextarc] = res[node]

                in_degree[nextarc] -= 1
                if in_degree[nextarc] == 0:
                    queue.append(nextarc)

        return res

if __name__ =='__main__':
    richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
    quiet = [3,2,5,4,6,1,7,0]
    res = Solution().loudAndRich(richer=richer,quiet=quiet)
    print(res)