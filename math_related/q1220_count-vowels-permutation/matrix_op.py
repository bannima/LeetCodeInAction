#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: matrix_op.py
@time: 2022/1/17 9:17 PM
@desc: 
"""
import numpy as np


class Solution:
    def countVowelPermutation(self,n):
        mod = 1e9 + 7
        matrix = np.mat([
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0],
        ])
        init = np.array([1, 1, 1, 1, 1])
        init = np.expand_dims(init, axis=1)

        for i in range(n - 1):
            init = matrix * init
            init = init % mod

        return int(int(sum(init)) % mod)






