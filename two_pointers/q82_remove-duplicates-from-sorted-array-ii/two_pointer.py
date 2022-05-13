#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: two_pointer.py
@time: 2022/5/13 10:10 PM
@desc: 
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        f,s = len(nums)-1,len(nums)-1
        while(s>=0):
            if nums[s]==nums[f]:
                if f-s==2:
                    del nums[f]
                    f-=1
            else:
                f = s
            s -=1
        return len(nums)