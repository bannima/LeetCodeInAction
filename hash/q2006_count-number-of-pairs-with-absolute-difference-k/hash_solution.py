#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: hash_solution.py
@time: 2022/2/10 8:42 PM
@desc: 
"""
from collections import Counter
class Solution:
    def countKDifference(self, nums, k: int) -> int:
        counter = Counter()#表示下标在j之前，其各个值的统计个数
        res = 0
        for j in range(len(nums)):
            t = nums[j]
            res += counter[t-k]
            res += counter[t+k]
            counter[t] +=1
        return res
