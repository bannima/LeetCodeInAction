#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: sort_two_pointer.py
@time: 2022/4/28 7:15 PM
@desc: 
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda asv: asv[0])
        res = []
        left, right = intervals[0]
        for inter in intervals[1:]:
            if inter[0] <= right:
                right = max(right, inter[1])
            else:
                res.append([left, right])
                left, right = inter
        res.append([left, right])
        return res



