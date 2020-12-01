#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_solution.py
Description: 
Author: Barry Chow
Date: 2020/11/30 9:58 PM
Version: 0.1
"""
from .solution import Solution

class Test:
    def test_solution(self):
        s = Solution()
        cands = [4,4,2,1,4,2,2,1,3]
        target = 6
        res = s.combinationSum2(cands,target)
        assert res==[]