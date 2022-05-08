#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: prefix_sum.py
@time: 2022/5/8 10:47 PM
@desc: 
"""
from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        print(prefix_sum)
        max_sum = -1
        # L在M的左侧, i表示L区间的右边界,j表示M区间的右边界
        for i in range(firstLen-1, len(nums) - secondLen):
            for j in range(i+secondLen, len(nums)):
                # L: nums[i-firstlen:i]  M: nums[j-secondLen:j]
                tmp = (prefix_sum[i] - prefix_sum[i - firstLen +1] + nums[i-firstLen+1]) + (prefix_sum[j] - prefix_sum[j - secondLen+1]+nums[j-secondLen+1])
                max_sum = max(max_sum, tmp)
        # L在M的右侧，i表示M区间的右边界,j表示L区间的右边界
        for i in range(secondLen - 1, len(nums) - firstLen):
            for j in range(i + firstLen, len(nums)):
                # L: nums[i-firstlen:i]  M: nums[j-secondLen:j]
                tmp = (prefix_sum[i] - prefix_sum[i - secondLen + 1] + nums[i - secondLen + 1]) + (
                            prefix_sum[j] - prefix_sum[j - firstLen +1] + nums[j - firstLen +1])
                max_sum = max(max_sum, tmp)
        return max_sum

if __name__ == '__main__':
    nums = [0,6,5,2,2,5,1,9,4]
    firstLen = 1
    secondLen  = 2
    res = Solution().maxSumTwoNoOverlap(nums,firstLen,secondLen)
    print(res)


