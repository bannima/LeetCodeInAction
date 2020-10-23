#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution2.py
Description: 
Author: Barry Chow
Date: 2020/10/23 4:59 PM
Version: 0.1
"""
class Solution(object):
    def trap(self, height):
        """
        按照列计算面积，对于每一列，只需要找到左边最高的墙和右边最高的墙即可
        :type height: List[int]
        :rtype: int
        """
        area = 0
        for j in range(1,len(height)-1):
            #左边最高的墙
            left = max(height[0:j])
            #右边最高的墙
            right = max(height[j+1:])
            if left > height[j] and right >height[j]:
                #加入这一列的面积
                area += min(left,right)-height[j]
        return area
