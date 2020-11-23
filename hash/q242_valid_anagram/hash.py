#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: hash.py
Description: 
Author: Barry Chow
Date: 2020/11/23 10:55 PM
Version: 0.1
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for cs in s:
            if cs in dic:
                dic[cs]+=1
            else:
                dic[cs]=1
        for cs in t:
            if cs in dic:
                dic[cs]-=1
                if dic[cs]==0: del dic[cs]
            else:
                return False
        return sum(dic.values())==0