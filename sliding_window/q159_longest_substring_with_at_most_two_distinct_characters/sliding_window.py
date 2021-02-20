#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: sliding_window.py
Description: 
Author: Barry Chow
Date: 2021/2/20 11:45 AM
Version: 0.1
"""
'''
class CharMap:
    def __init__(self):
        self.map = {}

    def in(self,char):
        if char in map:
            self.map[char]+=1
        else:
            self.map[char]=1

    def out(self,char):
        if char in self.map:
            if self.map[char]==1:
                del self.map[char]
            else:
                self.map[char]-=1
        else:
            raise ValueError(char+' not in map')

    def num_chars(self):
        return len(self.map.keys())

'''


class Solution:
    def num_chars(self, s):
        return len(set(list(s)))

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0;
        r = 0
        max_len = -1
        while (r <= len(s)):
            if self.num_chars(s[l:r]) <= 2:
                if (r - l) > max_len:
                    max_len = r - l
                r += 1
            elif self.num_chars(s[l:r]) > 2:
                l += 1
        return max_len