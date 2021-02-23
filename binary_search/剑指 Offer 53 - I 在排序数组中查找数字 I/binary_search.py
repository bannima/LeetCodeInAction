#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: binary_search.py
Description: 
Author: Barry Chow
Date: 2021/2/23 11:33 AM
Version: 0.1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(target):
            l = 0
            r = len(nums)-1
            while(l<=r):
                mid = (l+r)//2
                if nums[mid]<target:
                    l = mid+1
                #查找左边界
                elif nums[mid]==target:
                    r = mid-1
                else:
                    r = mid-1
            return l

        return helper(target+1)-helper(target)
