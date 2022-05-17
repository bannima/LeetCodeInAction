#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: left_right.py
@time: 2022/5/17 9:49 PM
@desc: 
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        k = 1
        for i in range(len(nums)):
            ans[i] = k
            k *= nums[i]
        k = 1
        for i in reversed(range(len(nums))):
            ans[i] *= k
            k *= nums[i]
        return ans

