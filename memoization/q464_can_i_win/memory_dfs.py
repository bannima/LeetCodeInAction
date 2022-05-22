#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: memory_dfs.py
@time: 2022/5/22 4:15 PM
@desc: 
"""

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        memory = {}
        def dfs(state,cur):
            """ 计算当前state下 进行选择是否会取胜 """
            #当前选择下的当前数组和
            if state not in memory:
                for i in range(maxChoosableInteger):
                    ans = False
                    #表示第i位未被选择 且
                    if state>>i & 1 ==0:
                        #选择i是否会取胜
                        if cur+i+1 >=desiredTotal:
                            ans = True
                            break
                        #我选择i后，对手是否会输
                        if dfs(state | (1<<i),cur+i+1)==False:
                            ans = True
                            break
                memory[state] = ans
            return memory[state]
        return False if (maxChoosableInteger+1)*maxChoosableInteger//2 < desiredTotal else dfs(0,0)

