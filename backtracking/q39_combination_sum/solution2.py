#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution2.py
Description: 
Author: Barry Chow
Date: 2021/3/22 4:30 PM
Version: 0.1
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #设立查找元素的起点，即后面新增的元素都不小于该起点，来避免重复元素
        def find(beign,tgt,path):
            if tgt==0:
                res.append(path)
                return
            if tgt<0:
                return
            for num in candidates:
                if num>=beign:
                    find(num,tgt-num,path+[num])
        find(0,target,[])
        return res