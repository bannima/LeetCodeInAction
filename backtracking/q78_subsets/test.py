#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test.py
Description: 
Author: Barry Chow
Date: 2020/12/2 3:49 PM
Version: 0.1
"""
from .solution import Solution

class Test:
    def test(self):
        nums = [1,2,3]
        s = Solution()
        res = s.subsets(nums)
        assert res==[]
