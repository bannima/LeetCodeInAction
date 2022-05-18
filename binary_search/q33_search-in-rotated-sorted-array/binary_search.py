#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: binary_search.py
@time: 2022/5/18 8:04 PM
@desc: 
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # 左边数组 升序，numsp[m]是左边最大的数字
            elif nums[l] <= nums[m]:
                # 左边数据升序，且目标值比nums[m]更小，则一定在左边有序子数组中
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                # 左边数据升序，且目标值比nums[m]更小，则一定不在左边数组，有可能在右边数组
                else:
                    l = m + 1
            # 右边数组是升序，nums[r]>nums[m],nums[m]是右边最小的数
            elif nums[r] >= nums[m]:
                # 目标值比nums[m]大，则一定在右边：
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                # 目标值比nums[m]小，则一定在左边：
                else:
                    r = m - 1
        return -1

if __name__ =='__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    res = Solution().search(nums,target)
    print(res)