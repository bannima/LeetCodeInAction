
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/26 9:20 PM
@desc: 
"""

from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # dp[l] 表示x轴第l个位置当前石子最大高度，默认为0
        dp = {}
        gloabal_high = 0
        ans = []
        for left_i,sidel_i in positions:
            # 计算[lefti:lefti + sideLengthi]的最大高度为下一个石子的起始点高度
            ls,rs = left_i,left_i + sidel_i
            max_l = 0
            for l,r in dp:
                # overlap condation,排除掉不想交的情况
                if not (r<=ls or rs<=l):
                    max_l = max(max_l,dp[(l,r)])
            # 计算当前最大值
            gloabal_high = max(gloabal_high,max_l + sidel_i)
            ans.append(gloabal_high)
            # 以该起始点的最低高度，修改dp
            dp[(left_i,left_i+sidel_i)] = max_l + sidel_i
        print(dp)
        return ans