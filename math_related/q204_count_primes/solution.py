#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/4 10:25 PM
Version: 0.1
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        tmp = [True]*n
        count = 0
        for i in range(2,n):
            if tmp[i]:
                count+=1
                j=i
                while(j<n):
                    tmp[j]=False
                    j+=i

        return count

