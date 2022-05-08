#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: sliding_window.py
@time: 2022/5/8 4:48 PM
@desc:
"""
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_zero = 0
        l = 0
        max_interval = -1
        for r,v in enumerate(nums):
            if v==0:
                num_zero+=1
            if num_zero<=1:
                max_interval = max(max_interval,r-l)
            else:
                while(l<=r and num_zero>1):
                    if nums[l]==0:
                        num_zero-=1
                    l+=1
        return max_interval

if __name__ == '__main__':
    nums = [0,1,1,1,0,1,1,0,1]
    res = Solution().longestSubarray(nums)
    print(res)