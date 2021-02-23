#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: binary.py
Description: 
Author: Barry Chow
Date: 2021/2/23 8:46 PM
Version: 0.1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l = mid+1
        return -1

