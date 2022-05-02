#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: topological_sort_dfs.py
@time: 2022/5/2 2:48 PM
@desc: topological sorting with dfs
"""
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0]*numCourses
        adjvec = [[] for _ in range(numCourses)]
        # init adjvec and in_degree
        for req in prerequisites:
            # pre node -> next arc
            adjvec[req[1]].append(req[0])
            in_degree[req[0]]+=1
        # init queue
        queue = [node for node in range(numCourses) if in_degree[node]==0]
        # bfs
        while queue:
            node = queue.pop(0)
            numCourses-=1
            for nextarc in adjvec[node]:
                # remove relation
                #adjvec[node].remove(nextarc)
                # update in-degree
                in_degree[nextarc]-=1
                # add queue in 0 indegree
                if in_degree[nextarc]==0:
                    queue.append(nextarc)
        return numCourses==0

if __name__ == '__main__':
    num = 5
    preqs = [[1, 4], [2, 4], [3, 1], [3, 2]]
    res = Solution().canFinish(numCourses=num,prerequisites=preqs)
    print(res)

