#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/24 4:01 PM
Version: 0.1
"""
class Solution(object):
    def reverseString(self, s):
        """
        双指针法
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while(i<j):
            char = s[j]
            s[j]=s[i]
            s[i] =char
            i+=1
            j-=1
