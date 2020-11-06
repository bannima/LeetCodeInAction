#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/6 6:36 PM
Version: 0.1
"""
from collections import Counter


class Solution:
    def slowestKey(self, releaseTimes, keysPressed) -> str:
        counter = {}
        counter[keysPressed[0]] = releaseTimes[0]

        for i in range(1, len(releaseTimes)):
            key = keysPressed[i]
            if key in counter:
                counter[key] = max(counter[key], releaseTimes[i] - releaseTimes[i - 1])
            else:
                counter[key] = releaseTimes[i] - releaseTimes[i - 1]

        res = sorted(counter.items(), key=lambda asv: asv[1], reverse=True)
        key, time = res[0]

        for k, t in res[1:]:
            if time == t and k > key:
                key = k
        return key
