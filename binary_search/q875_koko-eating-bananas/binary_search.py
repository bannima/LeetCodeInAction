#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: binary_search.py
@time: 2022/6/7 10:12 PM
@desc: 
"""
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def min_hours(k):
            """
            返回吃掉当前k下，吃掉这些香蕉的小时数h
            单次需要向上取整
            """
            ans = 0
            for pile in piles:
                ans += (pile+ k-1)//k
            return ans
        # 二分查找满足条件的最小的k
        l,r = 1, max(piles)
        while l<r:
            m = (l+r)//2
            # 使用m作为k，需要消耗的小时数字， >h 表示太慢，下一个区间为[m+1,r]
            if min_hours(m)>h:
                l=m+1
            # <=h 表示速度过快或者刚好，下一个区间为[l,m]
            else:
                r = m
        return l




