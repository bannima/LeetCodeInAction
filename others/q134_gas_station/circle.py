#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: circle.py
Description: 
Author: Barry Chow
Date: 2020/11/19 5:25 PM
Version: 0.1
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def check(start):
            capacity = gas[start]
            for j in range(len(gas)):
                capacity -= cost[(j + start) % len(gas)]
                if capacity < 0: return (j + start) % len(gas)
                capacity += gas[(j + start + 1) % len(gas)]
            return -1

        i = 0
        while (i < len(gas)):
            res = check(i)
            if res == -1:
                return i
            else:
                i = max(res, i) + 1
        return -1


