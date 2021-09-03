#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution2.py
Description: 
Author: Barry Chow
Date: 2021/9/2 9:15 PM
Version: 0.1
"""

class Solution:
    def maxSubArray(self, nums) -> int:
        s = 0
        max_s = -float('inf')
        for i in range(len(nums)):
            s += nums[i]
            max_s = max(max_s,s)
            if s<0:
                s=0
        return max_s

if __name__ =='__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution().maxSubArray(nums)
    assert s==6