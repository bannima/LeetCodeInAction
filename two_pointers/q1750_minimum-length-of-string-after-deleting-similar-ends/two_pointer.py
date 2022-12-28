#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def minimumLength(self, s: str) -> int:
        """
        两个指针从左右两边往中间查找，如果字符不等则跳出循环，
        每一步找到最大的前后缀，并进行比较
        """
        i,j = 0,len(s)-1
        while i<j and s[i]==s[j]:
            while i+1<j and s[i]==s[i+1]:
                i+=1
            while j-1>i and s[j]==s[j-1]:
                j-=1
            i,j = i+1,j-1
        return max(0,j-i+1)