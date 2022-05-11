#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: hash.py
@time: 2022/5/11 11:05 PM
@desc: 
"""

class Solution:
    def numTrees(self, n: int) -> int:
        counter = {1:1}
        def num_cand(nodes):
            if len(nodes) <=1:
                return 1
            if len(nodes) in counter:
                return counter[len(nodes)]
            count = 0
            for i,node in enumerate(nodes):
                left = nodes[:i]
                right = nodes[i+1:]
                count += num_cand(left) * num_cand(right)
            counter[len(nodes)]=count
            return count
        return num_cand(list(range(n)))

