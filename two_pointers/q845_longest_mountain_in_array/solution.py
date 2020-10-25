#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/25 2:45 PM
Version: 0.1
"""

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        peek = -1
        left = 0
        max_len = 0
        for j in range(1,len(A)):
            #上升
            if A[j]>A[j-1]:
                #有山顶则更新left，
                if peek>left:
                    left = j-1
            #下降
            elif A[j]<A[j-1]:
                #若j-left==1表示数组到目前还没有出现peek
                if j-left==1:
                    left = j
                #有山顶，记录最大值
                elif peek>left:
                    length = j-left+1
                    max_len = length if length>max_len else max_len
                #无山顶，更新peek
                else:
                    peek=j-1
                    length = j-left+1
                    max_len = length if length>max_len else max_len
            #持平
            else:
                left = j

        return max_len



