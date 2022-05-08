#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/5/8 3:31 PM
@desc: 
"""
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        输入输出的空间不属于额外空间，可以在输入数组中用数字的正负来表示该位置所对应数字是否已经出现过。
        遍历输入数组，给对应位置的数字取相反数，如果已经是负数，说明前面已经出现过，直接放入输出数组。
        """
        res = []
        for i,n in enumerate(nums):
            n = abs(n)
            if nums[n-1] >0:
                nums[n-1] = -1*nums[n-1]
            else:
                res.append(n)
        return res
