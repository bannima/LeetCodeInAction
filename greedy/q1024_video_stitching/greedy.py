#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: greedy.py
Description: 
Author: Barry Chow
Date: 2020/10/24 9:53 AM
Version: 0.1
"""
class Solution(object):
    def videoStitching(self, clips, T):
        """
        贪心算法，每次都选取以i，i从0开始，开始最大的长度的片段
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        i = 0
        res = []
        flag = True
        while (i<T and flag):
            max_length = -1
            cur_clip = -1
            for j in range(len(clips)):
                #包含以i为起点的所有视频子片段，查找以i为起点，最大长度的视频
                if clips[j][0]<=i and clips[j][1]>i:
                    if (clips[j][1]-clips[j][0])>max_length:
                        max_length = clips[j][1]-i
                        cur_clip = j
            #找不到片段，返回false
            if cur_clip==-1:
                flag = False
            #找到了片段，存进数组
            res.append(cur_clip)
            #这个片段的最右边值为i的计算值
            i = clips[cur_clip][1]
        return len(res) if flag else -1

