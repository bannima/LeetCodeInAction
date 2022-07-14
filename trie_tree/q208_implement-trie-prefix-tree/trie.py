#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie.py
@time: 2022/7/14 8:53 PM
@desc: 
"""


class Trie:

    def __init__(self):
        self.trie = {}
        self.indices = 'indices'

    def insert(self, word: str) -> None:
        cur_trie = self.trie
        for i,c in enumerate(word):
            if c not in cur_trie:
                cur_trie[c] = {}
            cur_trie = cur_trie[c]
        # i==len(word)-1
        if self.indices not in cur_trie:
            cur_trie[self.indices] = []
        cur_trie[self.indices].append(word)

    def search(self, word: str) -> bool:
        cur_trie = self.trie
        for i,c in enumerate(word):
            if c not in cur_trie:
                return False
            cur_trie = cur_trie[c]
        if self.indices not in cur_trie or word not in cur_trie[self.indices]:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur_trie = self.trie
        for i,c in enumerate(prefix):
            if c not in cur_trie:
                return False
            cur_trie = cur_trie[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

