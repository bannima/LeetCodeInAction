#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: monotonous_stack.py
Description: 
Author: Barry Chow
Date: 2021/3/7 5:06 PM
Version: 0.1
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)
        for i in range(len(nums)*2):
            i = i%len(nums)
            if not len(stack):
                stack.append(i)
            else:
                while(len(stack)!=0 and nums[stack[-1]]<nums[i]):
                    res[stack.pop()]=nums[i]
                stack.append(i)
        return res