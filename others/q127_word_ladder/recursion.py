#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: recursion.py
Description: 
Author: Barry Chow
Date: 2020/11/5 9:43 AM
Version: 0.1
"""


class Solution:
    '''
    递归算法，超时时间限制

    '''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        max_left = self.ladderL(beginWord, endWord, wordList)
        if max_left == float('-inf'):
            return 0
        else:
            return len(wordList) - max_left + 1

    def ladderL(self, beginWord, endWord, wordList):
        if beginWord == endWord:
            return len(wordList)
        max_Left = float('-inf')
        for word in wordList:
            if self.match(beginWord, word):
                # beginWord = word
                word_l = copy.copy(wordList)
                word_l.remove(word)
                max_Left = max(max_Left, self.ladderL(word, endWord, word_l))
        return max_Left

    def match(self, word1, word2):
        res = 0
        for a, b in zip(word1, word2):
            if a != b:
                res += 1
        return res == 1

