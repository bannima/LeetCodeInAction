#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: modify.py
Description: 
Author: Barry Chow
Date: 2020/11/19 9:20 PM
Version: 0.1
"""

class Solution:
    '''
    原地修改，秒啊
    '''
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index]>0:
                nums[index] = -1*nums[index]
        res = []
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
