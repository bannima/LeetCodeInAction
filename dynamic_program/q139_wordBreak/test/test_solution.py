#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: test_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/21 3:19 PM
Version: 0.1
"""
from dynamic_program.q139_wordBreak.solution import Solution
from dynamic_program.q139_wordBreak.dp_solution import Dp_Solution

class Test():
    def test(self):
        s = Solution()
        words = "leetcode"
        wordDict = ["leet","code"]
        res = s.wordBreak(words,wordDict)
        assert res==True

    def test_dp(self):
        words = "leetcode"
        wordDict = ["leet", "code"]
        res = Dp_Solution().wordBreak(words,wordDict)
        assert res == True

