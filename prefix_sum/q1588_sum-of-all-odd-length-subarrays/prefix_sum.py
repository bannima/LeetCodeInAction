#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: prefix_sum.py
@time: 2022/5/8 11:47 PM
@desc: 
"""

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum = []
        for n in arr:
            if len(prefix_sum)==0:
                prefix_sum.append(n)
            else:
                prefix_sum.append(n+prefix_sum[-1])
        total_sum = prefix_sum[-1]
        for k in range(3,len(arr)+1,2):
            print(k)
            for i in range(len(arr)-k+1):
                total_sum += prefix_sum[i+k-1]-prefix_sum[i] + arr[i]
        return total_sum


