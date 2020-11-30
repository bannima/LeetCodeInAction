#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/30 3:48 PM
Version: 0.1
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def isSum(num, trg, paths):
            if num == trg:
                ans = paths + [num]
                ans.sort()
                try:
                    ans.remove(0)
                except ValueError:
                    pass
                if ans not in res:
                    res.append(ans)
            else:
                for cand in candidates:
                    if cand <= trg:
                        isSum(cand, trg - num, paths + [num])

        isSum(0, target, [])
        return res
