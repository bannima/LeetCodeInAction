#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: analytical.py
Description: 
Author: Barry Chow
Date: 2021/2/18 11:43 AM
Version: 0.1
"""
import math
class Solution:
    '''
    函数解析法，满足条件的区间化为起始点为i，终点为y，则求和公式可计算delta，
    delta需要满足大于等于0，且sqrt（delta）需要为偶数（因为根需要为整数）
    '''
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for i in range(1,target//2+1):
            delta = 1-4*i+4*i*i+8*target
            if delta>=0:
                sqrt_delta = math.sqrt(delta)
                if sqrt_delta*sqrt_delta==delta and (sqrt_delta-1)%2==0:
                    y = int((-1+sqrt_delta)/2)
                    res.append(list(range(i,y+1)))
        return res
