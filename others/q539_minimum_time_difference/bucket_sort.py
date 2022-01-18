#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: bucket_sort.py
@time: 2022/1/18 7:25 PM
@desc: 
"""


class Solution:
    def findMinDifference(self, timePoints):
        def key(timepoint):
            hour = int(timepoint.split(':')[0])
            time = int(timepoint.split(':')[1])
            return hour * 60 + time

        map = {}
        for timepoint in timePoints:
            if key(timepoint) not in map:
                map[key(timepoint)] = 0
                map[key(timepoint) + 60 * 24] = 0
            map[key(timepoint)] += 1
            map[key(timepoint) + 60 * 24] += 1

        if len(map) > 24 * 60:
            return 0
        min_interval = 60 * 24
        last = -1
        print(map)
        for t in range(60 * 24 * 2):
            if t not in map:
                continue
            if map[t] == 1:
                if last != -1:
                    min_interval = min(min_interval, t - last)
                    print(min_interval, t, last)
                last = t
            else:
                return 0
        return min_interval

