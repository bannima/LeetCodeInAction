#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: xor.py
Description: 
Author: Barry Chow
Date: 2020/11/19 8:35 PM
Version: 0.1
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        if len(nums)>1:
            for n in nums[1:]:
                res = res ^ n
        return res