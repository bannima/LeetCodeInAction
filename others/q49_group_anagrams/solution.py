#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/16 11:14 AM
Version: 0.1
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def transfer(char):
            lc = list(char)
            lc.sort()
            return ''.join(lc)
        dic = {}
        for s in strs:
            key = transfer(s)
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        return list(dic.values())