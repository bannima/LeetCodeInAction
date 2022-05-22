#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp-meomory.py
@time: 2022/5/22 5:23 PM
@desc: 
"""
from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def dfs(array, s1, s2, chooser):
            """返回可选array下，chooser=【1，2】选择两端数字的赢家结果，归并原则为只要有一种情况chooser赢则返回true，都输则为false"""
            # print(array,s1,s2,chooser)
            if len(array) == 0:
                return s1 >= s2 if chooser == 1 else s1 < s2

            cand_ids = [0, -1] if len(array) >= 2 else [0]
            for id in cand_ids:
                c_array = array + []
                val = c_array.pop(id)
                if chooser == 1:
                    ans = dfs(c_array, s1 + val, s2, 2)
                else:
                    ans = dfs(c_array, s1, s2 + val, 1)
                # 当对手结果为失败时，自己才能赢
                if not ans:
                    return not ans
            return False

        return dfs(nums, 0, 0, 1)





