#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/25 10:59 AM
@desc: 
"""

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        #定义dp[a]为p中所有以字符a结尾的子串中，最长子串的长度
        # 如p=zab，则dp[z]=1,dp[a]=2,dp[b]=3
        dp = {}
        k =0
        for i,v in enumerate(p):
            if i>0 and (ord(p[i])-ord(p[i-1]))%26==1: # ord(p[i])-ord(p[i-1])) in [1,-25]
                k+=1
            else:
                k=1
            dp[v] = max(k,dp.get(v,0)) #保存最大
        #print(dp)
        return sum(dp.values())
