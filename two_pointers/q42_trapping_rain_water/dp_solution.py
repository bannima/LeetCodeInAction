#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/23 7:50 PM
Version: 0.1
"""
class Solution(object):
    def trap(self, height):
        """
        动态规划法，max_left[i]表示到height[0:i-1](注意不含height[i])的最大值
        计算方便，减少重复计算

        :type height: List[int]
        :rtype: int
        """
        if len(height)==0:
            return 0

        max_left = [0]*len(height)
        max_left[0]=height[0]

        max_right = [0]*len(height)
        max_right[-1]= height[-1]
        for j in reversed(range(len(height)-1)):
            max_right[j] = max(max_right[j+1],height[j])
        area = 0
        for i in range(1,len(height)-1):
            #更新第i个高度左边墙的最大值
            max_left[i] = max(max_left[i-1],height[i])
            #可以计算单个列的面积，
            if height[i]<max_left[i-1] and height[i]<max_right[i+1]:
                area += min(max_left[i-1],max_right[i+1])-height[i]

        return area



