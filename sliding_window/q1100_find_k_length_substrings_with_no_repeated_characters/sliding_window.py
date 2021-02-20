#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/20 7:57 PM
Version: 0.1
"""

from collections import Counter


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        pos = {}
        l = r = 0
        count = 0
        while (r < len(S)):
            if S[r] not in pos:
                pos[S[r]] = r
            else:
                # 删除l到pos[S[r]]的元素信息
                start = pos[S[r]] + 1
                for i in range(l, pos[S[r]] + 1):
                    del pos[S[i]]
                l = start
                pos[S[r]] = r

            if len(pos) == K:
                count += 1
                del pos[S[l]]
                l += 1
            r += 1

        return count



