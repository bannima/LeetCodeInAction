#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: bs_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/24 11:39 AM
Version: 0.1
"""


class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        """
        排序加二分查找，先对drinks排序，在对staple中每个元素，查找drinks中第一个大于x-stap的值的位置，
        :type staple: List[int]
        :type drinks: List[int]
        :type x: int
        :rtype: int
        """

        drinks.sort()
        count = 0

        for stap in staple:
            # 二分查找
            if x - stap < 0:
                continue
            left = 0
            right = len(drinks)
            while (left < right):
                mid = (left + right) / 2
                if (x - stap) >= drinks[mid]:
                    left = mid + 1
                else:
                    right = mid
            count += left

        return int(count % (1e9 + 7))






