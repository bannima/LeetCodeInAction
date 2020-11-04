#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/4 5:16 PM
Version: 0.1
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start = newInterval[0]
        end = newInterval[1]
        res = []

        if len(intervals) == 0:
            res.append(newInterval)
            return res

        find_left = False
        find_right = False

        for i, (left, right) in enumerate(intervals):
            # 还没找到start所在的区间
            if not find_left:
                # 起始点在当前区间和上一个区间之间
                if start < left:
                    find_left = True

                # 起始点在这个区间
                elif start <= right:
                    find_left = True
                    start = left

                # 起始点不在这个区间，在后面区间
                elif start > right:
                    res.append(intervals[i])

            # 找到start所在的区间，再寻找end
            if not find_right:
                # end在当前区间和之前区间之间
                if end < left:
                    res.append([start, end])
                    res.append([left, right])
                    find_right = True

                # end在当前区间内
                elif end <= right:
                    end = right
                    res.append([start, end])
                    find_right = True

                # end在之后的区间
                elif end > right:
                    # 若是最后一个元素，需要保存值
                    if len(intervals) - 1 == i:
                        res.append([start, end])


            else:
                res.append(intervals[i])

        return res









