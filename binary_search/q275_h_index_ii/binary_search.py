#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: binary_search.py
Description: 
Author: Barry Chow
Date: 2021/2/27 7:32 PM
Version: 0.1
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==0:
            return 0
        l = 0
        r = len(citations)-1
        while(l<=r):
            mid = (l+r)//2
            if citations[mid]<len(citations)-mid:
                l = mid+1
            elif citations[mid]>len(citations)-mid:
                r = mid-1
            else:
                return len(citations)-mid

        return len(citations)-l
