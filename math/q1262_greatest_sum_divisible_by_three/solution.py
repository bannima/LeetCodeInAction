#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/17 7:10 PM
Version: 0.1
"""


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        remin = [val % 3 for val in nums]
        summary = sum(remin)
        ind = summary % 3
        if ind == 0:
            return sum(nums)
        res = []
        first = float('inf')
        second = float('inf')
        third = float('inf')
        for i, val in enumerate(remin):
            # 1个1 或者1个2
            if val == ind and first == float('inf'):
                first = i
                res.append(sum(nums) - nums[i])
            elif val == (3 - ind):
                if second == float('inf'):
                    second = i
                elif third == float('inf'):
                    third = i

            if first != float('inf') and third != float('inf'):
                res.append(sum(nums) - nums[second] - nums[third])
                break
        return max(res)

