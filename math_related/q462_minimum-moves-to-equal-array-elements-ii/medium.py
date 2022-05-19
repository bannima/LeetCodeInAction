#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: medium.py
@time: 2022/5/19 11:23 AM
@desc: 
"""
from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[len(nums)//2]
        times = [abs(x-n) for n in nums]
        return sum(times)