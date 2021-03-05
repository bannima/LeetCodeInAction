#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: hash_pre_sum.py
Description: 
Author: Barry Chow
Date: 2021/3/5 4:38 PM
Version: 0.1
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        dic = {0: 1}
        count = 0
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in dic:
                count += dic[pre - k]

            if pre in dic:
                dic[pre] += 1
            else:
                dic[pre] = 1

        return count



