#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: greedy.py
@time: 2022/5/25 6:01 PM
@desc: 
"""

from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        totalValues = list(map(lambda x:x[0]+x[1],zip(aliceValues,bobValues)))
        totalValues.sort(reverse=True)
        # alice每次选择一个石子i，会产生两种效果，一是给自己石子价值增加aliceValues[i],二是降低了对手的石子价值bobValues[i],
        # 每个人都应该贪心选择 石子和最大的，alice先选择
        alice_select = totalValues[::2]
        # alice选择的和，石子中包括了bob的石子部分，应该减去，bobValues包括alice选择的石子部分，和bob选择的石子部分，二者差为 最终的两个人分数差
        ans = sum(alice_select) - sum(bobValues)
        if ans>0:
            return 1
        elif ans<0:
            return -1
        else:
            return 0
