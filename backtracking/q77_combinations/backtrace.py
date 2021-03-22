#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: backtrace.py
Description: 
Author: Barry Chow
Date: 2021/3/22 4:50 PM
Version: 0.1
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = list(range(1,n+1))
        res = []
        #每次从candidates中找到比begin大的数字进行回溯
        def find(begin,depth,path):
            if depth==k:
                res.append(path)
                return
            for num in candidates:
                if num>begin:
                    find(num,depth+1,path+[num])
        find(0,0,[])
        return res