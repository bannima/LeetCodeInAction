#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/30 9:49 PM
Version: 0.1
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def find(trg,paths,remain):
            if trg==0 and paths not in res:
                    res.append(paths)
                    return
            #for num in candidates[remain:]:
            for pos in range(remain,len(candidates)):
                num = candidates[pos]
                if pos>=1 and num==candidates[pos-1] and trg==target:
                    continue
                if num<=trg:
                    find(trg-num,paths+[num],pos+1)
                if num>trg:
                    return
        find(target,[],0)
        return res