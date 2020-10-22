#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_dp.py
Description: 
Author: Barry Chow
Date: 2020/10/22 10:45 AM
Version: 0.1
"""

from dynamic_program.q392_isSubsequence.dp_solution import Solution

class Test_Dp():
    def test(self):
        s = Solution()
        res = s.isSubsequence('acb',"ahbgdc")
        assert res==False
