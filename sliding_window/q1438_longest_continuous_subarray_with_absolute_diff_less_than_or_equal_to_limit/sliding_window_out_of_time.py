#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window_out_of_time.py
Description: 
Author: Barry Chow
Date: 2021/2/21 10:19 AM
Version: 0.1
"""


class Solution:
    '''
    超过时间了
    '''
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        # 判断nums是否满足limit 的性质
        def in_limit(nums):
            min_v = min(nums)
            max_v = max(nums)
            for n in nums:
                if n < max_v - limit or n > min_v + limit:
                    return False
            return True

        l = 0
        r = 1

        min_v = nums[0]
        max_v = nums[0]
        max_len = r - l

        while (r < len(nums)):
            # 新增窗口右端节点

            # 新增节点，在区间范围内
            if nums[r] >= max_v - limit and nums[r] <= min_v + limit:

                min_v = min(min_v, nums[r])
                max_v = max(max_v, nums[r])

                if r - l + 1 > max_len:
                    max_len = r - l + 1

            # 新增节点不满足区间范围，需要进行左端窗口左移，直到满足性质
            else:
                for j in range(l, r + 1):
                    if not in_limit(nums[l:r + 1]):
                        l += 1
                    else:
                        break

                min_v = min(nums[l:r + 1])
                max_v = max(nums[l:r + 1])

            r += 1

        return max_len








