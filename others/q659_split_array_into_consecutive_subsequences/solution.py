#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/4 9:56 PM
Version: 0.1
"""


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        tmp = [[nums[0]]]
        for i in range(1, len(nums)):
            find = False
            for t in tmp:
                # 只有一个值
                if len(t) == 1 and (nums[i] - t[-1]) == 1:
                    t.append(nums[i])
                    find = True
                    break
                # 有两个值，第一个值是起始，第二个值是连续子串的最大值
                elif (nums[i] - t[-1]) == 1:
                    t[-1] = nums[i]
                    find = True
                    break

            if not find:
                tmp.insert(0, [nums[i]])

        for t in tmp:
            if len(t) == 1 or (len(t) == 2 and (t[-1] - t[0]) < 2):
                return False

        return True





