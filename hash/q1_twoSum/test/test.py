#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test.py
Description: 
Author: Barry Chow
Date: 2020/10/22 1:19 PM
Version: 0.1
"""
from hash.q1_twoSum.solution import Solution

class Test():
    def test(self):
        nums = [2, 7, 11, 15]
        target = 9
        s = Solution()
        res = s.twoSum(nums,target)
        assert res==[1,0]