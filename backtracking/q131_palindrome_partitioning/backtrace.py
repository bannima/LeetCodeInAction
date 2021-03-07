#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: backtrace.py
Description: 
Author: Barry Chow
Date: 2021/3/7 11:36 AM
Version: 0.1
"""

from copy import copy
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(string):
            l = 0
            r = len(string)-1
            while(l<=r):
                if string[l]!=string[r]:
                    return False
                l+=1
                r-=1
            return True

        def backtrace(path,string):
            if len(string)==0:
                res.append(path)
            else:
                for i in range(len(string)):
                    if is_palindrome(string[:i+1]):
                        path_c = copy(path)
                        path_c.append(string[:i+1])
                        backtrace(path_c,string[i+1:])
        backtrace([],s)
        return res
