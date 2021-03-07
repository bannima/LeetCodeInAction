#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: monotonous_stack.py
Description: 
Author: Barry Chow
Date: 2021/3/7 5:20 PM
Version: 0.1
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            if len(stack) == 0:
                stack.append(i)
            else:
                while (len(stack) != 0 and nums2[i] > nums2[stack[-1]]):
                    n = nums2[stack.pop()]
                    if n in nums1:
                        res[nums1.index(n)] = nums2[i]
                stack.append(i)
        return res

