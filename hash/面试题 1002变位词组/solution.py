#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/10/2 6:27 PM
Version: 0.1
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def hash_str(string):
        #     return ''.join(sorted(list(string)))
        def hash_str(string):
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                      101]  # 26个质数
            key = 1
            for c in list(string):
                key *= primes[ord(c) - ord('a')]
            return key

        res = dict()

        for string in strs:
            key = hash_str(string)
            if key not in res:
                res[key] = []
            res[key].append(string)
        return list(res.values())

