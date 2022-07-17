#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: traceback.py
@time: 2022/7/17 8:16 PM
@desc: 
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def traceback(word,depth,l,r):
            if depth==2*n:
                # check legalness and remove depulicates
                if l==r:
                    ans.append(word)
                # reach max depth, must return
                return
            # 注意一旦r>l表示闭括号比开括号多的时候，都为非法组合，直接剪纸
            elif l>n or r>n or r>l:
                return
            else:
                traceback(word+'(',depth+1,l+1,r)
                traceback(word+')',depth+1,l,r+1)
        traceback("",0,0,0)
        return ans

