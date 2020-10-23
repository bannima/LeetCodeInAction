#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/23 1:36 PM
Version: 0.1
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        双指针法，i表示前指针，j表示后指针，对j进行遍历，若sum>=s,则对i进行后移
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = len(nums) + 1
        i = 0
        sum = 0
        for j in range(len(nums)):
            sum += nums[j]
            while (sum >= s):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                sum -= nums[i]
                i += 1
        return min_len if min_len != (len(nums) + 1) else 0

