#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/7 6:31 PM
Version: 0.1
"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c) + 1)):
            b = math.sqrt(c - a * a)
            if b == int(b):
                return True
        return False


if __name__ =='__main__':
    res = Solution().judgeSquareSum(999999999)
    assert res==False