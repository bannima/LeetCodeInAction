#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: hash_presum.py
Description: 
Author: Barry Chow
Date: 2021/3/5 5:06 PM
Version: 0.1
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre = 0
        dic = {0: -1}

        for i in range(len(nums)):
            pre += nums[i]

            #
            for v in dic:
                if k != 0:
                    if (pre - v) % k == 0 and i - dic[v] >= 2:
                        return True
                else:
                    if pre == v and i - dic[v] >= 2:
                        return True

            # 记录首次出现位置，方便计算
            if pre not in dic:
                dic[pre] = i
        return False
