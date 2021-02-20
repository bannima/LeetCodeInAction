#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: two_pointers.py
Description: 
Author: Barry Chow
Date: 2021/2/20 11:10 AM
Version: 0.1
"""
class Solution:
    '''
    双指针法
    '''
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum = -1
        l = 0;r = len(nums)-1
        while(l<r):
            s = nums[l]+nums[r]
            if s<k:
                if s>sum:
                    sum = s
                l+=1
            else:
                r-=1
        return sum