#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie.py
@time: 2022/7/14 10:10 PM
@desc: 
"""
class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.idx = "idx"

    def addWord(self, word: str) -> None:
        cur_trie = self.trie
        for i,c in enumerate(word):
            if c not in cur_trie:
                cur_trie[c] = {}
            cur_trie = cur_trie[c]
        cur_trie[self.idx] = True

    def search(self, word: str) -> bool:
        def match(cur_trie,i):
            if not cur_trie:
                return False
            if i==len(word):
                return cur_trie.get(self.idx,False)
            c = word[i]
            if c!='.':
                return c in cur_trie and match(cur_trie[c],i+1)
            # c=='.'
            else:
                for key in cur_trie.keys():
                    if key!=self.idx and match(cur_trie[key],i+1):
                        return True
            return False

        return match(self.trie,0)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


