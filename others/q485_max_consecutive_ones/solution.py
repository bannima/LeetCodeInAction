#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/24 5:13 PM
Version: 0.1
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0
        for i in nums:
            #首次出现1，或者连续出现1
            if i==1:
                count+=1
                if count>max_count:
                    max_count = count
            else:
                count=0
        return max_count