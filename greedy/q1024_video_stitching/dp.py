#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp.py
Description: 
Author: Barry Chow
Date: 2020/10/24 10:36 AM
Version: 0.1
"""
class Solution(object):
    def videoStitching(self, clips, T):
        """
        DP法
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        #dpp[i]表示到0-i所需的最少片段数
        dp = [0]+[float('inf')]*T
        for t in range(1,T+1):
            for i in range(len(clips)):
                #若当前子片段包含了节点i，即子片段左边小于等于i，右边大于i，则比较
                #所有满足条件子片段的左端dp值，再加当前子片段，即为dp[i]的值
                if clips[i][0]<t and clips[i][1]>=t:
                    dp[t] = min(dp[t],dp[clips[i][0]]+1)

        return dp[T] if dp[T]!=float('inf') else -1

