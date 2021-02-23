#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: binary_search.py
Description: 
Author: Barry Chow
Date: 2021/2/23 11:44 AM
Version: 0.1
"""


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        # 找到首次出现值小于target的位置,左边界
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                r = mid - 1
            else:
                r = mid - 1
        return nums[l + len(nums) // 2] == target if l + len(nums) // 2 < len(nums) else False


