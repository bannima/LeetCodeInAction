#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/19 4:57 PM
Version: 0.1
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def check_start(i):
            capacity = gas[i]
            for j in range(len(gas)):
                pos = (i + j) % len(gas)
                capacity -= cost[pos]
                if capacity < 0: return False
                capacity += gas[(i + j + 1) % len(gas)]
            return True

        if sum(gas) < sum(cost): return -1

        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue
            elif check_start(i):
                return i
        return -1




