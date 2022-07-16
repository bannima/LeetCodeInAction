#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie.py
@time: 2022/7/16 10:45 AM
@desc: 
"""
from typing import List

class TrieTree():
    def __init__(self):
        self.trie = {}
        self.ind = "ind"

    def insert(self,word:str):
        cur_trie = self.trie
        for i,c in enumerate(word):
            if not c in cur_trie:
                cur_trie[c] = {}
            cur_trie = cur_trie[c]
        cur_trie[self.ind] = True

    def search(self,word:str):

        def match(cur_trie,i,flag)->bool:
            if len(word)==i:
                return self.ind in cur_trie and flag==1
            c = word[i]
            ans = False
            for new_c in cur_trie:
                if new_c != self.ind:
                    ans = ans or match(cur_trie[new_c],i+1,flag+1 if new_c!=c else flag)
            return ans

        # 查找 如果替换任意一个字母，字典树是否存在该单词
        return match(self.trie,0,0)

class MagicDictionary:

    def __init__(self):
        self.trie = TrieTree()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord)




