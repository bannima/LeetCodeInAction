#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/20 4:33 PM
Version: 0.1
"""

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        pointer = []
        l=0;r=0
        max_len = -1
        while(r<len(A)):
            if A[r]==0:
                if len(pointer)<K:
                    pointer.append(r)
                else:
                    if K==0:
                        l=r+1
                    else:
                        l = pointer[0]+1
                        pointer.remove(pointer[0])
                        pointer.append(r)
            r+=1
            if r-l>max_len:
                max_len = r-l
        return max_len

