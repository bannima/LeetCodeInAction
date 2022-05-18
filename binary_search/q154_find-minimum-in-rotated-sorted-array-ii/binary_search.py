#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: binary_search.py
@time: 2022/5/18 9:32 PM
@desc: 
"""
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l<r:
            m = (l+r)//2
            # 左序列严格升序，一定在右序列中
            if nums[m]>nums[r]:
                l = m+1
            # 右子树严格升序，在做序列及nums[m]中
            elif nums[m]<nums[r]:
                r = m
            # nums[l]==nums[r]==nums[m],则缩短查找区间[left,right]为[left,right-1]，
            else:
                r = r-1
        return nums[r]

if __name__ == '__main__':

    nums = [3,3,1,3]
    res = Solution().findMin(nums)
    print(res)