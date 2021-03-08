#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp.py
Description: 
Author: Barry Chow
Date: 2021/3/8 2:37 PM
Version: 0.1
"""

from copy import copy


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dp表示每一步的可能结果和出现的次数
        if nums[0] == 0:
            dp = {nums[0]: 2}
        else:
            dp = {nums[0]: 1, -1 * nums[0]: 1}
        for i in range(len(nums) - 1):
            target = {}
            for k, t in dp.items():
                if k + nums[i + 1] in target:
                    target[k + nums[i + 1]] += t
                else:
                    target[k + nums[i + 1]] = t

                if k - nums[i + 1] in target:
                    target[k - nums[i + 1]] += t
                else:
                    target[k - nums[i + 1]] = t

            dp = copy(target)

        return dp.get(S) if (S in dp) else 0

