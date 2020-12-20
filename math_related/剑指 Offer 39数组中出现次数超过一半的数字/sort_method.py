#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sort_method.py
Description: 
Author: Barry Chow
Date: 2020/12/19 7:37 PM
Version: 0.1
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]