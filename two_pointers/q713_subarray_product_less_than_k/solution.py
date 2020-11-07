#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/7 3:31 PM
Version: 0.1
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        res = 0
        product = 1
        left = 0
        for right,val in enumerate(nums):
            product *= nums[right]
            while product>=k:
                product/=nums[left]
                left+=1
            res += right-left+1
        return res