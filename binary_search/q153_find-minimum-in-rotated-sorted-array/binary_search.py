#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: binary_search.py
@time: 2022/5/18 9:05 PM
@desc: 
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l<r:
            m = (l+r)//2
            # 左边数组是升序，且 nums[m]比右区间值小
            if nums[l]<=nums[m] and nums[m]>nums[r]:
                l = m+1
            else:
                r= m
        return nums[r]

if __name__ == '__main__':
    nums = [3,4,5,1,2]
    res = Solution().findMin(nums)
    print(res)
