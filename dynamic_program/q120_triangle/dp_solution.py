#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/19 8:22 PM
Version: 0.1
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==1:
            return triangle[0][0]
        dp = [[0]*len(triangle[-1]) for _ in range(len(triangle))]
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i==0:
                    dp[i][j]=triangle[0][0]
                elif j==0:
                    dp[i][j] = dp[i-1][j]+triangle[i][j]
                elif j==(len(triangle[i])-1):
                    dp[i][j] = dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        return min(dp[-1])
