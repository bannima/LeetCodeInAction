#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/22 1:19 PM
Version: 0.1
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_set = {}
        for i,val in enumerate(nums):
            if hash_set.get(target-nums[i]) is not None:
                return [i,hash_set[target-nums[i]]]
            hash_set[val] = i