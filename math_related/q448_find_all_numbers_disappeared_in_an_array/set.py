#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: set.py
Description: 
Author: Barry Chow
Date: 2020/11/19 9:06 PM
Version: 0.1
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums)+1))-set(nums))