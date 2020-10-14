#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: center_solution.py
Description:  用中心扩散法解决最长回文子串问题
Author: Barry Chow
Date: 2020/10/14 9:17 PM
Version: 0.1
"""

class Center_Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        max_length = 0
        max_pos = 0

        for pos in range(0, len(s)-1):
            # odd case
            odd_pos, odd_length = self._center_palindrome(s, pos, pos)
            # even case
            even_pos, even_length = self._center_palindrome(s, pos, pos + 1)

            if even_length > max_length:
                max_length = even_length
                max_pos = even_pos
            if odd_length > max_length:
                max_length = odd_length
                max_pos = odd_pos

        return s[max_pos:max_pos + max_length + 1]

    def _center_palindrome(self, s, i, j):
        '''
        从i和j的中间位置不停的往两边扩散,返回能扩散的最大长度
        '''
        if s[i]!=s[j]:
            return i,0

        while ((i - 1 >= 0) and ((j + 1 )<= (len(s) - 1))):
            if s[i - 1] == s[j + 1]:
                i = i - 1
                j = j + 1
            else:
                break
        return i, j - i

