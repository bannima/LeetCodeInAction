#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: bit_op.py
@time: 2022/7/17 5:10 PM
@desc: 
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n<=0 else  (n & (n-1)==0)

