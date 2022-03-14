#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: pre_sum.py
@time: 2022/3/14 10:40 PM
@desc: 
"""

class Solution:
    def platesBetweenCandles(self, s: str, queries):
        # 前缀和
        pre_sum = [0] * len(s)
        # 每个查询点的第一个左边的蜡烛位置
        lefts = [-1] * len(s)
        # 每一个查询点的第一个右边蜡烛的位置
        rights = [-1] * len(s)
        valid_left = -1
        valid_right = -1
        for i, val in enumerate(s):
            if val == '|':
                if valid_left != -1:
                    pre_sum[i] = pre_sum[i - 1] + (i - valid_left - 1)
                valid_left = i

                if valid_right != -1:
                    rights[valid_right + 1:i + 1] = [i] * (i - valid_right)
                else:
                    rights[0:i + 1] = [i] * (i + 1)

                valid_right = i

            else:
                pre_sum[i] = pre_sum[i - 1]
            lefts[i] = valid_left
        print(lefts)
        print(rights)
        print(pre_sum)
        res = []
        for query in queries:
            l, r = query
            # 必须满足，左查询点右边第一个蜡烛，和右边查询点左边第一个蜡烛，之间的差值作为最终结果
            # 找到左查询点第一个右边的蜡烛
            l = rights[l]
            # 找到右查询点第一个左边的蜡烛
            r = lefts[r]

            if l < r:
                res.append(pre_sum[r] - pre_sum[l])
            else:
                res.append(0)
        return res