#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: sliding_window.py
@time: 2022/5/6 12:20 AM
@desc: 
"""
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, cur_s = 0,0
        max_s = float('inf') * -1
        for r,v in enumerate(nums):
            if r<k-1:
                cur_s+=v
                continue
            cur_s+=v
            if r-l>k-1:
                cur_s -= nums[l]
                l+=1
            max_s = max(max_s,cur_s)
        return max_s/float(k)

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    res = Solution().findMaxAverage(nums,k)
    print(res)
