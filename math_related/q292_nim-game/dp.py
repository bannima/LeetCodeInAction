#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp.py
Description: 
Author: Barry Chow
Date: 2021/9/26 10:20 PM
Version: 0.1
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        queue = [True, True, True, False]
        if n <= len(queue):
            return queue[n - 1]

        for i in range(4, n):  # len(res)==4
            queue.append(False)
            for j in range(-3, 0):  # j=-1,-2,-3
                if queue[j - 1] == False:
                    queue[-1] = True
                    break
            queue.pop(0)

        return queue[-1]