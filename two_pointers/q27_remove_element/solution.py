#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/8 11:25 AM
Version: 0.1
"""


class Solution:
    def removeElement(self, nums, val):
        i = 0
        j = 0
        while (j < len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

if __name__ =='__main__':
    res = Solution().removeElement([0,1,2,2,3,0,4,2],2)
    assert res==5