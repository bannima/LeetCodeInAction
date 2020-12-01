#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/1 7:55 PM
Version: 0.1
"""

import copy


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def permute(paths, remain):
            if len(paths) == len(nums) and paths not in res:
                res.append(paths)
                return
            left = copy.copy(remain)
            for pos, num in enumerate(left):
                if pos >= 1 and num == left[pos - 1]:
                    continue
                remain_c = copy.copy(left)
                remain_c.remove(num)
                permute(paths + [num], remain_c)

        permute([], nums)
        return res
