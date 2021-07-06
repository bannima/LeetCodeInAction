#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sort_two_pointer.py
Description: 
Author: Barry Chow
Date: 2021/7/6 1:56 PM
Version: 0.1
"""

class Solution:
    def threeSum(self, nums) :
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            L = i+1
            R = len(nums)-1
            while(L<R):
                if nums[i]+nums[L]+nums[R]==0:
                    res.append([nums[i],nums[L],nums[R]])
                    while L<R and nums[L]==nums[L+1]:
                        L+=1
                    while L<R and nums[R]==nums[R-1]:
                        R-=1
                    L+=1
                    R-=1
                elif nums[i]+nums[L]+nums[R]>0:
                    R-=1
                elif nums[i]+nums[L]+nums[R]<0:
                    L+=1
        return res

if __name__ =='__main__':
    s = Solution()
    nums = [-2,0,0,2,2]
    res = s.threeSum(nums)
    assert res ==[[-2,0,2]]