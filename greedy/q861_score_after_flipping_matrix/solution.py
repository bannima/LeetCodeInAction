#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/12/7 3:13 PM
Version: 0.1
"""

import math
class Solution:
    def matrixScore(self, A):
        m = len(A)
        n = len(A[0])
        #行变换，第1列的值，全部换成1
        for i in range(m):
            if A[i][0]==0:
                A[i] = [(1-A[i][j]) for j in range(n)]
        #列变换，从第二列开始，若0的个数大于1的个数，则转换
        for j in range(1,n):
            #对于第j列元素
            count = sum([A[i][j] for i in range(m)])
            if count<(m/2):
                for i in range(m):
                    A[i][j] = 1-A[i][j]
        #统计元素值
        res = 0
        for i in range(m):
            for j in range(n):
                res += A[i][j]*math.pow(2,n-j-1)
        return res

if __name__ =='__main__':
    A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    s = Solution()
    res = s.matrixScore(A)
    assert res ==39