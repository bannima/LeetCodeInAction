#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution1.py
Description: 
Author: Barry Chow
Date: 2020/10/23 4:19 PM
Version: 0.1
"""

class Solution(object):
    def trap(self, height):
        """
        按照行进行计算，找到每一行开始计算面积的起始位置和结束计算面积的条件
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0

        max_height = max(height)
        start = 0
        area = 0

        for row in range(1,max_height+1):
            #标识何时开始计数
            start = -1
            tmp = 0
            for j in range(len(height)):
                #查找开始计算的位置
                if start== -1 and height[j]>=row:
                    start = j
                    continue
                #找到第一个计算位置，开始计算面积
                if start>=0:
                    if height[j]<row:
                        tmp+=1
                    #只有当右边有比row不小于的墙时，才把这一行存进去，同时把这一行的面积清零
                    if height[j]>=row:
                        area += tmp
                        tmp = 0
        return area
