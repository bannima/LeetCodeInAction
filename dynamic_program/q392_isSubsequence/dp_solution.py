#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dp_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/22 10:45 AM
Version: 0.1
"""


class Solution(object):
    def isSubsequence(self, s, t):
        """
        暴力解法
        start表示上次匹配结束的点
        count表示已匹配单词数目

        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        count = 0
        start = 0
        for i in range(len(s)):
            for j in range(start,len(t)):
                if s[i]==t[j]:
                    count+=1
                    if count==len(s):
                        return True
                    start = j+1
                    break

        return False