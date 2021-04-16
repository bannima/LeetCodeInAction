#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/4/16 5:19 PM
Version: 0.1
"""
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<0:return False
        while(n%2==0): n = n//2
        while(n%3==0): n = n//3
        while(n%5==0): n = n//5
        return n==1