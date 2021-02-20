#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/18 11:47 AM
Version: 0.1
"""
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        sum = 0
        l = 1;r=1
        res = []
        while l<=target//2:
            if sum<target:
                sum+=r
                r+=1
            elif sum>target:
                sum-=l
                l+=1
            else:
                res.append(list(range(l,r)))
                sum-=l
                l+=1

        return res

