#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/2/10 7:57 PM
@desc: 
"""
from math import gcd

class Solution:
    def simplifiedFractions(self, n: int):
        return ["{}/{}".format(j,i) for i in range(2,n+1) for j in range(1,i) if gcd(i,j)==1]