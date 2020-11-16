#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/16 8:34 PM
Version: 0.1
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people,key=lambda x:(-x[0],x[1]))
        res =[]
        for p in people:
            if p[1]>=len(res):
                res.append(p)
            else:
                res.insert(p[1],p)
        return res