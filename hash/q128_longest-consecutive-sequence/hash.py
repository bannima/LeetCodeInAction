#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: hash.py
@time: 2022/4/29 2:49 PM
@desc: 
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        max_length = 0
        for num in nums:
            if num not in dic:
                left = dic.get(num-1,0)
                right = dic.get(num+1,0)
                cur_length = 1 + left + right
                max_length = max(max_length,cur_length)

                dic[num] = cur_length
                dic[num-left] = cur_length
                dic[num+right] = cur_length
        return max_length