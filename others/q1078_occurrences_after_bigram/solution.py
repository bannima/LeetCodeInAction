#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/25 3:18 PM
Version: 0.1
"""

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text = text.split()
        res = []
        for j in range(1,len(text)):
            if text[j-1]==first and text[j]==second:
                if j+1<=len(text)-1:
                    res.append(text[j+1])
        return  res

