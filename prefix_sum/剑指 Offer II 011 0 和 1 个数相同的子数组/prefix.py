#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: prefix.py
@time: 2022/5/9 3:42 PM
@desc: 
"""
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counter = {0: -1}
        pre_sum = 0
        max_len = 0
        for r, n in enumerate(nums):
            n = 1 if n == 1 else -1
            pre_sum += n
            if pre_sum in counter:
                max_len = max(max_len, r - counter[pre_sum])
            else:
                counter[pre_sum] = r
        return max_len

if __name__ == '__main__':
    nums = [0,1]
    res = Solution().findMaxLength(nums)
    print(res)