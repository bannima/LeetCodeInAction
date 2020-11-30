#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_solution.py
Description: 
Author: Barry Chow
Date: 2020/11/24 10:56 AM
Version: 0.1
"""
from .solution import Solution

class Test:
    def test(self):
        s = Solution()
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        res = s.spiralOrder(matrix)