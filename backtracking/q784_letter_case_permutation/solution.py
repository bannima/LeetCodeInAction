#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/3/23 9:36 PM
Version: 0.1
"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        res = []

        # index表示搜索的起点，path表示不含index之前的路径
        def backtrace(index, path):
            if index == len(S):
                res.append(path)
                return
            if S[index].isalpha():
                backtrace(index + 1, path + S[index].upper())
                backtrace(index + 1, path + S[index].lower())
            else:
                backtrace(index + 1, path + S[index])

        backtrace(0, "")
        return res



