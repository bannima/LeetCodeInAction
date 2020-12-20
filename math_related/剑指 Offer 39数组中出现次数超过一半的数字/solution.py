#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: hash法
Author: Barry Chow
Date: 2020/12/19 7:33 PM
Version: 0.1
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        dic = {}
        for n in nums:
            if n in dic:
                dic[n]+=1
                if dic[n] > len(nums)//2:
                    return n
            else:
                dic[n]=1