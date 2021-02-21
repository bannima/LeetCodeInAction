#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/21 3:34 PM
Version: 0.1
"""

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)==1: return 1
        elif len(arr)==2:
            return 2 if arr[1]!=arr[0] else 1

        l = 0
        r = 1
        max_l = float('-inf')

        #init value
        flag = 0
        if arr[r]>arr[r-1]:
            flag = 1
        elif arr[r]<arr[r-1]:
            flag = -1

        while(r<len(arr)-1):
            r+=1
            if arr[r]>arr[r-1]:
                if flag != -1:
                    l = r-1
                    flag = 1
                else:
                    flag = -1*flag
            elif arr[r]<arr[r-1]:
                if flag != 1:
                    l = r-1
                    flag = -1
                else:
                    flag = -1*flag

            elif arr[r]==arr[r-1]:
                flag = 0
                l = r
            max_l = max(max_l,r-l+1)

        return max_l









