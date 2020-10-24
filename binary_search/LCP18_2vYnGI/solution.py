#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/24 11:20 AM
Version: 0.1
"""


class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        解法：先对drinks进行排序，在对每个staple元素，查找drinks中小于等于drink的元素个数
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """
        count = 0
        # arr[i]表示当前主食中，小于等于i的个数
        arr = [0] * x
        for stap in staple:
            if stap < x:
                arr[stap] += 1

        # arr表示，在主食stap确定下，可以选择的所有饮料数目
        for i in range(1, x):
            arr[i] += arr[i - 1]

        # 遍历所有饮料，统计所有可行解
        for drink in drinks:
            if drink < x:
                count += arr[x - drink]
        return int(count % (1e9 + 7))
