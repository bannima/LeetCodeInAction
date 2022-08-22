#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack
        stack = [0]
        max_area,n = 0,len(heights)
        heights = [0]+heights +[0]
        for i in range(1,n+2):
            while heights[i]<heights[stack[-1]]:
                cur_id = stack.pop(-1)
                width = i-stack[-1]-1
                max_area = max(max_area,width*heights[cur_id])
            stack.append(i)
        return max_area
