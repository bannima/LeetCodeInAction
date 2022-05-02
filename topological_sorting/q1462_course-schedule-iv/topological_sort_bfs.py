#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: topological_sort_bfs.py
@time: 2022/5/2 5:14 PM
@desc: 
"""
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:
        adjvec = [[] for _ in range(numCourses)]
        pre = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        # init adjvec
        for req in prerequisites:
            adjvec[req[0]].append(req[1])
            in_degree[req[1]] += 1
        # init queue
        queue = [node for node in range(numCourses) if in_degree[node] == 0]

        # bfs
        while queue:
            node = queue.pop(0)
            for nextarc in adjvec[node]:
                pre[nextarc] = list(set(pre[nextarc] + pre[node] + [node]))
                in_degree[nextarc] -= 1
                if in_degree[nextarc] == 0:
                    queue.append(nextarc)
        # traverse the answer
        res = []
        for query in queries:
            if query[0] in pre[query[1]]:
                res.append(True)
            else:
                res.append(False)
        return res


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[2, 3], [2, 1], [0, 3], [0, 1]]
    queries = [[0, 1], [0, 3], [2, 3], [3, 0], [2, 0], [0, 2]]
    res = Solution().checkIfPrerequisite(numCourses=4,prerequisites=prerequisites,queries=queries)
    print(res)
