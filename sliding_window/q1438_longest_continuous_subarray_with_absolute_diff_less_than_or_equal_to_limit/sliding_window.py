#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/21 10:19 AM
Version: 0.1
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        l = 0
        r = 1

        min_v = nums[0]
        max_v = nums[0]
        max_len = r - l

        while (r < len(nums)):
            min_v = min(min_v, nums[r])
            max_v = max(max_v, nums[r])

            # 新增节点，在区间范围内
            if nums[r] >= max_v - limit and nums[r] <= min_v + limit:

                if r - l + 1 > max_len:
                    max_len = r - l + 1

            # 新增节点不满足区间范围，需要进行左端窗口左移，直到满足性质
            else:
                for j in reversed(range(l, r)):
                    l = j + 1

                    # 从r开始，往左找到第一个不满足性质的点
                    if nums[j] > min_v + limit or nums[j] < max_v - limit:
                        break

                min_v = min(nums[l:r + 1])
                max_v = max(nums[l:r + 1])

            r += 1

        return max_len