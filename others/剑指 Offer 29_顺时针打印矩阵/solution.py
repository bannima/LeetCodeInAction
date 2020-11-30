#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/24 10:56 AM
Version: 0.1
"""

class Solution:
    def spiralOrder(self, matrix) :
        m = len(matrix)
        n = len(matrix[0])
        flag = [[True] * n for _ in range(m)]
        stack = [(matrix[0][0], (0, 0))]
        flag[0][0] = False
        res = []
        while (stack):
            cur, (i, j) = stack.pop()
            res.append(cur)
            # right
            if j < n - 1 and flag[i][j + 1]:
                stack.append((matrix[i][j + 1], (i, j + 1)))
                flag[i][j + 1] = False
            # down
            elif i < n - 1 and flag[i + 1][j]:
                stack.append((matrix[i + 1][j], (i + 1, j)))
                flag[i + 1][j] = False

            # left
            elif j - 1 >= 0 and flag[i][j - 1]:
                stack.append((matrix[i][j - 1], (i, j - 1)))
                flag[i][j - 1] = False

            # upper
            elif i - 1 >= 0 and flag[i - 1][j]:
                stack.append((matrix[i - 1][j], (i - 1, j)))
                flag[i - 1][j] = False

        return res

