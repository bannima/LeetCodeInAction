#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/9 9:07 PM
Version: 0.1
"""
import heapq
from math import sqrt, pow

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(point):
            return sqrt(pow(point[0], 2) + pow(point[1], 2))

        q = []
        for point in points:
            heapq.heappush(q, (dist(point), point))

        res = []
        for i in range(K):
            res.append(heapq.heappop(q)[1])
        return res
