#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_sl.py
Description: 
Author: Barry Chow
Date: 2020/11/6 6:36 PM
Version: 0.1
"""
from .solution import Solution
class Test():
    def test(self):
        s = Solution()
        res = s.slowestKey([1,2,3],"aba")
        assert  res=='a'