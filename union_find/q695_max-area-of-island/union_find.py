#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: union_find.py
@time: 2022/5/3 4:56 PM
@desc: 
"""
from typing import List


class Position():
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def id(self):
        #return "{}-{}".format(self.i,self.j)
        return self.i * 50 +self.j

    def __hash__(self):
        return self.id()

    def __eq__(self, other):
        return self.id() == other.id()

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        parents = {}
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        # init  parents
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    parents[Position(i,j)] = Position(i,j)

        def legal_pos(i, j):
            if (i >= 0 and i < m) and (j >= 0 and j < n):
                return True
            return False

        # find parent
        # def find(i):
        #     while i!=parents[i]:
        #         i = parents[i]
        #     return i
        def find(i):
            if i==parents[i]:
                return i
            else:
                parents[i] = find(parents[i])
                return parents[i]

        # union op
        def union(i,j):
            parents[find(i)] = parents[find(j)]

        # merge
        for i in range(m):
            for j in range(n):
                for dir in dirs:
                    ni, nj = i + dir[0], j + dir[1]
                    # connection between (i,j)--(ni,nj)
                    if grid[i][j] == 1 and legal_pos(ni, nj) and grid[ni][nj] == 1:
                        union(Position(i, j), Position(ni, nj))
        # res
        parent_ids = [find(node).id() for node in parents]
        return parent_ids.count(max(parent_ids,key=parent_ids.count)) if parent_ids else 0

if __name__ == '__main__':
    #grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid = [[0,0,0,0,0,0,0,0]]
    res = Solution().maxAreaOfIsland(grid)
    print(res)