#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/1 8:59 PM
Version: 0.1
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        res = []
        def combination(trg,k,paths,beign):
            if k==0 and trg==0 and paths not in res:
                res.append(paths)
                return
            if k==0:
                return
            for pos in range(beign,len(nums)):
                num = nums[pos]
                if num>trg:
                    return
                if num<=trg:
                    combination(trg-num,k-1,paths+[num],pos+1)
        combination(n,k,[],0)
        return res
