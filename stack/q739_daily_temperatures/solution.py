#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/12 8:25 PM
Version: 0.1
"""

class Solution:
    '''
    暴力法
    '''
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res =[]
        for i in range(len(T)):
            wait= 0
            for j in range(i,len(T)):
                if T[i]<T[j]:
                    wait = j-i
                    break
            res.append(wait)
        return res