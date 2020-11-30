#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/30 11:08 PM
Version: 0.1
"""

import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def perm(paths,remains):
            if len(remains)==0:
                res.append(paths)
                return
            for num in copy.copy(remains):
                remains.remove(num)
                perm(paths+[num],remains)
                remains.append(num)
        perm([],nums)
        return res