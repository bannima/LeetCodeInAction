#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/19 4:22 PM
Version: 0.1
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        if len(nums) <= 1: return
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                continue
            else:
                while (left < right):
                    if nums[left] != 0:
                        left += 1
                    else:
                        break

                swap(left, right)



