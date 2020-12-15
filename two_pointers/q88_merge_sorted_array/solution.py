#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/15 10:49 PM
Version: 0.1
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return
        i = m - 1
        j = n - 1
        for pos in reversed(range(m + n)):
            if j < 0:
                break
            elif i < 0:
                nums1[pos] = nums2[j]
                j -= 1

            elif nums2[j] > nums1[i]:
                nums1[pos] = nums2[j]
                j -= 1
            else:
                nums1[pos] = nums1[i]
                i -= 1

