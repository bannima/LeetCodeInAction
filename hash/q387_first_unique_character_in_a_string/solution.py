#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/22 1:41 PM
Version: 0.1
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        字典存储，如果重复则记为inf
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1

        pos = {}
        for i, char in enumerate(s):
            if char not in pos:
                pos[char] = i
            else:
                pos[char] = float('inf')

        res = sorted(pos.items(), key=lambda asv: asv[1])[0][1]

        return res if res != float('inf') else -1