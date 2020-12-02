#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/2 4:14 PM
Version: 0.1
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        def sub(i,tmp):
            res.append(tmp)
            for j in range(i,n):
                if (j-i)>=1 and nums[j]==nums[j-1]:
                    continue
                sub(j+1,tmp+[nums[j]])
        sub(0,[])
        return res