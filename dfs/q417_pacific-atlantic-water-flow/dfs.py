#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/4/28 4:00 PM
@desc: 
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def pos_legal(i, j):
            if (i < m and i >= 0) and (j < n and j >= 0):
                return True
            return False

        def search(starts):
            visited = set()

            def dfs(i, j):
                if (i, j) in visited: return
                visited.add((i, j))
                for dir in dirs:
                    ni, nj = i + dir[0], j + dir[1]
                    if pos_legal(ni, nj) and heights[i][j] <= heights[ni][nj]:
                        dfs(ni, nj)

            for pos in starts:
                dfs(pos[0], pos[1])
            return visited

        # pacific
        pacific = list(set([(0, i) for i in range(n)] + [(j, 0) for j in range(m)]))
        altantic = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]

        return list(search(pacific) & search(altantic))

if __name__ =='__main__':
    #heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    heights = [[1,2,3],[8,9,4],[7,6,5]]
    res = Solution().pacificAtlantic(heights)
    print(res)
