#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/2/26 7:38 PM
@desc: 
"""


class Solution:
    def findBall(self, grid):
        def traverse(c, grid):  # start from row 0
            for r in range(len(grid)):
                if grid[r][c] == 1:
                    if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:  # (1,1) go right
                        c = c + 1
                    elif c + 1 >= len(grid[0]):  # out of boundary
                        return -1
                    else:  # (1,-1)
                        return -1
                else:  # row[r][c]=-1
                    if c - 1 >= 0 and grid[r][c - 1] == -1:  # (-1,-1)
                        c = c - 1
                    elif c - 1 <= 0:  # out of boundary
                        return -1
                    else:  # (1,-1)
                        return -1
            return c

        res = []
        for c in range(0, len(grid[0])):
            res.append(traverse(c, grid))
        return res


