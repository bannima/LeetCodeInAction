#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/24 7:21 PM
Version: 0.1
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        '''
        双指针法，超过100%的用户
        '''

        max_length = -1
        # 翻转0的位置
        pos = -1
        # 最长连续1的左起点
        left = 0
        for j in range(len(nums)):
            # 首次使用
            if nums[j] == 0 and pos == -1:
                pos = j
            # 翻转已使用，区分两种情况，第一种是非两个连续的0，则left+1，当前翻转过来，
            # 第二种情况是连续的两个0，则left=j,当前翻转过来
            elif nums[j] == 0 and pos != -1:
                # 非连续的两个0情况,更新left为pos的下一个位置
                if pos != j - 1:
                    left = pos + 1
                    pos = j
                # 连续的两个0情况
                else:
                    left = j
                    pos = j
            # 统计最大长度
            length = j - left + 1
            if length > max_length:
                max_length = length
        return max_length
