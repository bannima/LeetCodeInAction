#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie.py
@time: 2022/7/16 9:32 AM
@desc: 
"""
from typing import List


class TrieTree():
    def __init__(self):
        self.trie = {}
        self.ind = 'indices'

    def insert(self, word: str):
        cur_trie = self.trie
        for i, c in enumerate(word):
            if c not in cur_trie:
                cur_trie[c] = {}
            cur_trie = cur_trie[c]
        cur_trie[self.ind] = True

    def search_max_pref(self, word: str):
        cur_trie = self.trie
        pref = []
        for i, c in enumerate(word):
            if c not in cur_trie:
                return []
            cur_trie = cur_trie[c]
            pref.append(c)
            # 找到最短的词根，若匹配则退出
            if self.ind in cur_trie and cur_trie[self.ind]:
                return pref
        return pref


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieTree()
        for word in dictionary:
            trie.insert(word)
        res = []
        for sent in sentence.split(" "):
            max_pref = trie.search_max_pref(sent)
            # print(sent,max_pref)
            res.append("".join(max_pref) if max_pref else sent)
        return " ".join(res)

if __name__ == '__main__':
    # dictionary =["cat","bat","rat"]
    # sentence = "the cattle was rattled by the battery"

    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"

    res = Solution().replaceWords(dictionary,sentence)
    print(res)









