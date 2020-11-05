#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: bfs.py
Description: 
Author: Barry Chow
Date: 2020/11/5 11:02 AM
Version: 0.1
"""
from collections import deque
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        queue = deque()
        queue.append((beginWord,1))
        mark = defaultdict(bool)
        mark[beginWord]=True

        while len(queue):
            cur_word,level = queue.popleft()
            for word in wordList:
                if cur_word==endWord:
                    return level
                if not mark[word] and self.match(cur_word,word):
                    queue.append((word,level+1))
                    mark[word]=True
        return 0

    def match(self,word1,word2):
        res = 0
        for a,b in zip(word1,word2):
            if a!=b:
                res+=1
            if res>1: return False
        return True

