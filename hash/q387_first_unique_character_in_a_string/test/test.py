#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test.py
Description: 
Author: Barry Chow
Date: 2020/10/22 1:42 PM
Version: 0.1
"""

from hash.q387_first_unique_character_in_a_string.solution import Solution

class Test():
    def test(self):
        s = Solution()
        assert s.firstUniqChar('leetcode')==0