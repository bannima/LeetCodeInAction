#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/6 9:03 PM
Version: 0.1
"""

from collections import defaultdict


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = defaultdict(list)

        for num in arr:
            # count binary 1 numbers
            count = 0
            for char in str(bin(num)):
                if char == '1':
                    count += 1
            dic[count].append(num)

        output = []
        for i in range(15):
            for num in sorted(dic[i]):
                output.append(num)

        return output
