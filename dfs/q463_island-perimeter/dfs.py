#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def is_legal_pos(ni, nj):
            if ni >= 0 and ni < m and nj >= 0 and nj < n:
                return True
            return False

        def dfs(i, j):
            # 从岛屿走到了边缘位置，周长+1
            if not is_legal_pos(i, j):
                return 1
            # 从岛屿走到了水的位置，周长+1
            elif grid[i][j] == 0:
                return 1
            # 从岛屿走到了岛屿，周长不变
            elif grid[i][j] == 2:  # 2
                return 0
            # mark visisted
            grid[i][j] = 2
            res = 0
            # equals to 1
            for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res += dfs(i + dir[0], j + dir[1])
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0


