#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window_sortedlist.py
Description: 
Author: Barry Chow
Date: 2021/2/21 11:10 AM
Version: 0.1
"""

from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList(nums[:k])
        if k%2==1:
            res = [window[k//2]]
        else:
            res = [(window[k//2]+window[k//2-1])/2]
        l = 0
        r = k
        while(r<len(nums)):
            window.add(nums[r])
            window.remove(nums[l])
            if k%2==1:
                res.append(window[k//2])
            else:
                res.append((window[k//2]+window[k//2-1])/2)
            r+=1
            l+=1
        return res