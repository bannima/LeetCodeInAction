#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/2 3:49 PM
Version: 0.1
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def sub(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                sub(j + 1, (tmp + [nums[j]]))

        sub(0, [])
        return res