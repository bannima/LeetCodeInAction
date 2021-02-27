#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: binary_search.py
Description: 
Author: Barry Chow
Date: 2021/2/27 6:09 PM
Version: 0.1
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while(l<r):
            mid = (l+r)//2
            if nums[mid]==nums[mid-1]:
                if (mid-1-l)%2==0:
                    l = mid+1
                else:
                    r = mid-2
            elif nums[mid]==nums[mid+1]:
                if (r-mid-1)%2==0:
                    r = mid-1
                else:
                    l = mid+2
            else:
                return nums[mid]

        return nums[l]