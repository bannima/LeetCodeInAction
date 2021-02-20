#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: force.py
Description: 
Author: Barry Chow
Date: 2021/2/18 11:23 AM
Version: 0.1
"""


class Solution:
    '''
    暴力枚举法，从1开始，到target//2+1，每次遍历数组，如果sum==target则记录
    注意range(i,j)包含头不包含尾为[i,i+1,..,j-2,j-1]
    '''
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for i in range(1, target // 2 + 1):
            sum = 0
            for j in range(i, target // 2 + 1 +1):
                sum += j
                if sum == target:
                    res.append(list(range(i, j + 1)))
                    break
                elif sum > target:
                    break
        return res
