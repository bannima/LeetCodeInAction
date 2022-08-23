#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def cal_max_area(heights):
            nheights = [0] + heights + [0]
            max_area, n = 0, len(nheights)
            stack = []
            for j in range(len(nheights)):
                while len(stack) >= 1 and nheights[stack[-1]] > nheights[j]:
                    cur_height = nheights[stack.pop(-1)]
                    width = j - stack[-1] - 1
                    max_area = max(max_area, width * cur_height)
                stack.append(j)
            return max_area

        m, n = len(matrix), len(matrix[0])
        heights, max_area = [0] * n, 0
        for i in range(m):
            for j in range(n):
                # update heigths array
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            # calculate max rectangle area with monotonic stack
            # print(heights)
            max_area = max(max_area, cal_max_area(heights))
        return max_area


