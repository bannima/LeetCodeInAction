#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_solution.py
Description: 
Author: Barry Chow
Date: 2020/12/2 4:15 PM
Version: 0.1
"""

from .solution import Solution

class Test:
    def test(self):
        s= Solution()
        nums = [1,2,2]
        res = s.subsetsWithDup(nums)
        assert res==[]