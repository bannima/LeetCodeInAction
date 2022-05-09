#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: prefix_sum_hash.py
@time: 2022/5/9 6:04 PM
@desc: 
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        counter = {0: 1}  # 表示子数组 前缀和 对应的次数
        res = 0
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in counter:
                res += counter[prefix_sum - k]
            if prefix_sum not in counter:
                counter[prefix_sum] = 0
            counter[prefix_sum] += 1
        return res


if __name__ =='__main__':
    nums = [1,1,1]
    k = 2
    res = Solution().subarraySum(nums,k)
    print(res)