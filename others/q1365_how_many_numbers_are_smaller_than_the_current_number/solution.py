#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/26 10:02 PM
Version: 0.1
"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort_nums = sorted(nums)
        counter = {}
        for i,num in enumerate(sort_nums):
            if num not in counter:
                counter[num]=i
        res = []
        for num in nums:
            res.append(counter[num])
        return res



