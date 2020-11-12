#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: stack.py
Description: 
Author: Barry Chow
Date: 2020/11/12 8:54 PM
Version: 0.1
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''
        用栈的解法，栈顶保存最小值，每次出现比栈顶元素大的时候，栈顶元素出栈
        '''

        stack = []
        res = [0]*len(T)
        for i,val in enumerate(T):
            if len(stack)==0:
                stack.append((val,i))
            else:
                #out stack
                while len(stack)>0 and val>stack[-1][0]:
                    val_c,i_c = stack.pop()
                    res[i_c] = i-i_c
                stack.append((val,i))
        #empty the stack
        while(len(stack)):
            val,i = stack.pop()
            res[i]=0

        return res

