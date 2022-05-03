#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: union_find.py
@time: 2022/5/3 7:20 PM
@desc: 
"""

from typing import List

class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        class Position():
            def __init__(self, i, j):
                self.i = i
                self.j = j

            def id(self):
                return self.i * 1000 + self.j

            def __hash__(self):
                return self.id()

            def __eq__(self, other):
                return self.id() == other.id()

        m, n = len(land), len(land[0])
        parents = {}
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),(-1,-1),(1,1),(-1,1),(1,-1)]
        # init parents
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    parents[Position(i, j)] = Position(i, j)

        def legal_pos(i, j):
            if (i >= 0 and i < m) and (j >= 0 and j < n):
                return True
            return False

        # find parent
        def find(pos):
            while parents[pos] != pos:
                pos = parents[pos]
            return pos

        # union operation
        def union(pos_i, pos_j):
            parents[find(pos_i)] = find(pos_j)

        # merge
        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    for dir in dirs:
                        ni, nj = i + dir[0], j + dir[1]
                        if legal_pos(ni, nj) and land[ni][nj] == 0:
                            union(Position(i, j), Position(ni, nj))
        # return format
        parents_id = [find(node).id() for node in parents]
        from collections import Counter
        return sorted(list(Counter(parents_id).values()))

if __name__ == '__main__':
    land = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
    res = Solution().pondSizes(land)
    print(res)