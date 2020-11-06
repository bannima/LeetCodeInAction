#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp.py
Description: 
Author: Barry Chow
Date: 2020/11/6 4:28 PM
Version: 0.1
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        # tails[i]表示当前长度为i+1的上升子序列中最小值
        tails = []
        tails.append(nums[0])

        for j in range(1, len(nums)):
            for i in reversed(range(len(tails))):
                if nums[j] < tails[i]:
                    if i != 0:
                        # 针对持平的情况，必须大于tail的前一个元素
                        if nums[j] <= tails[i - 1]:
                            continue
                    tails[i] = nums[j]
                elif nums[j] > tails[i] and i == len(tails) - 1:
                    tails.append(nums[j])

        return len(tails)



