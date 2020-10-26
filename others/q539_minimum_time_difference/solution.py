#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/26 10:38 PM
Version: 0.1
"""


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = []
        for time in timePoints:
            hour = int(time.split(':')[0])
            minute = int(time.split(":")[-1])
            minutes.append(60 * hour + minute)

        minutes.sort()

        min_minutes = 24 * 60
        for j in range(1, len(minutes)):
            tmp = minutes[j] - minutes[j - 1]
            if tmp < min_minutes:
                min_minutes = tmp

        return min_minutes if (minutes[0] + 24 * 60 - minutes[-1]) > min_minutes else (
                    minutes[0] + 24 * 60 - minutes[-1])


