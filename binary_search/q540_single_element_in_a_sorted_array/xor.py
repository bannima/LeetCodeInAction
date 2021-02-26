#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: xor.py
Description: 
Author: Barry Chow
Date: 2021/2/26 8:01 PM
Version: 0.1
"""

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
