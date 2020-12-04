#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/4 10:45 PM
Version: 0.1
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPre(str1,str2):
            common = []
            for a,b in zip(str1,str2):
                if a==b:
                    common.append(a)
                else:
                    break
            return ''.join(common)
        if len(strs)==0:
            return ''
        common = strs[0]
        for i in range(1,len(strs)):
            common = commonPre(common,strs[i])
        return common
