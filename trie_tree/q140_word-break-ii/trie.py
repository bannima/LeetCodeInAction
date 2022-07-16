#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie.py
@time: 2022/7/16 2:50 PM
@desc: 
"""
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def traceback(s,path):
            # stop condition
            if len(s)==0:
                ans.append(" ".join(path))
            for word in wordDict:
                if s.startswith(word):
                    traceback(s[len(word):],path+[word])
        traceback(s,[])
        return ans


