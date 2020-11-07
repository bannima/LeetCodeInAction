#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/7 4:30 PM
Version: 0.1
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(char):
            return char.lower() in ['a', 'e', 'i', 'o', 'u']

        left = 0;
        right = len(s) - 1
        s = list(s)
        while left < right:
            if isVowel(s[left]) and isVowel(s[right]):
                # swap
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            while (left < right and not isVowel(s[left])): left += 1
            while (left < right and not isVowel(s[right])): right -= 1

        return ''.join(s)