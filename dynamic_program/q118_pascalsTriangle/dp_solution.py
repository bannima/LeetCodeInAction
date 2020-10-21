#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/21 12:59 PM
Version: 0.1
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            tmp = [1] * (i + 1)
            for j in range(i):
                if j != 0 and j != i:
                    tmp[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(tmp)
        return res
