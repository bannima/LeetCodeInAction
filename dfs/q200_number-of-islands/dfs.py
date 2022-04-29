#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/4/29 5:44 PM
@desc: 
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        self.visited = [[0] * n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def legal_pos(i, j):
            if (i >= 0 and i < m) and (j >= 0 and j < n):
                return True
            return False

        def dfs(i, j ):
            for dir in dirs:
                ni, nj = i + dir[0], j + dir[1]
                # 表示该步骤合法 且为岛屿，且没有被访问过
                if legal_pos(ni, nj) and grid[ni][nj] == "1" and self.visited[ni][nj]==0:
                    self.visited[ni][nj] = 1
                    dfs(ni, nj)

        island_id = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and self.visited[i][j] == 0:
                    self.visited[i][j]=1
                    dfs(i, j)
                    island_id += 1

        return island_id

if __name__ == '__main__':
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    #grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    s = Solution().numIslands(grid)
    print(s)