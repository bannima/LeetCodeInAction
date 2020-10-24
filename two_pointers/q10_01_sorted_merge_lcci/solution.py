#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/24 3:41 PM
Version: 0.1
"""


class Solution(object):
    def merge(self, A, m, B, n):
        """
        逆指针法，从尾部开始比较
        ni
        :type A: List[int]
        :type m: int
        :type B: List[int]
        :type n: int
        :rtype: None Do not return anything, modify A in-place instead.
        """

        j = m - 1
        i = n - 1

        if i < 0:
            return

        for k in reversed(range(m + n)):
            # 若A和B的数组均可以比较
            if j >= 0 and i >= 0:
                if A[j] >= B[i]:
                    A[k] = A[j]
                    j -= 1
                else:
                    A[k] = B[i]
                    i -= 1
            # 若j<0，即A已经比较完了，将剩下的有序B全部复制到A里
            elif j < 0:
                A[k] = B[i]
                i -= 1

            # 若i<0,即B已经比较完了， A剩下的部分自然有序，什么也不需要做
            elif i < 0:
                continue

