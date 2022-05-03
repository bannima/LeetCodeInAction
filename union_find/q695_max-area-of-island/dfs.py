#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/5/3 3:02 PM
@desc: 
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        self.max_area = 0

        def legal_pos(i, j):
            if (i < m and i >= 0) and (j < n and j >= 0):
                return True
            return False

        def dfs(i, j, area):
            for dir in dirs:
                ni, nj = i + dir[0], j + dir[1]
                # legal pos,unvisited and island
                if legal_pos(ni, nj) and grid[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    self.max_area = max(self.max_area, area + 1)
                    area = dfs(ni, nj, area + 1)

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.max_area = max(self.max_area, 1)
                    visited[i][j] = 1
                    dfs(i, j, 1)

        for row in visited:
            print(row)

        return self.max_area

if __name__ == '__main__':
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    res = Solution().maxAreaOfIsland(grid)
    print(res)