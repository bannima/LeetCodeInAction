#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/16 10:33 AM
Version: 0.1
"""

class Solution:
    def maxSubArray(self, nums):
        total_max = cur_max = nums[0]
        before_max = 0
        for i in range(len(nums)):
            if before_max<0:
                cur_max = nums[i]
            else:
                cur_max = before_max+nums[i]

            before_max = cur_max

            total_max = max(total_max,cur_max)

        return total_max

if __name__ =='__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s = Solution().maxSubArray(nums)
    print(s)
    assert s==6


