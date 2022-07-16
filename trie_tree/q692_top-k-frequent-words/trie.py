#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie.py
@time: 2022/7/16 11:20 AM
@desc: 
"""
from typing import List


class TrieTree():
    def __init__(self, ):
        self.trie = {}
        self.ind = "ind"

    def insert(self, word: str):
        """
            insert the given word into trie tree.
        """
        cur_trie = self.trie
        for i, c in enumerate(word):
            if c not in cur_trie:
                cur_trie[c] = {}
            # set the prefix times
            # if self.cnt not in cur_trie:
            #     cur_trie[self.cnt] = 0
            # cur_trie[self.cnt] += 1
            # next level
            cur_trie = cur_trie[c]
        # set the leaf node flag
        if self.ind not in cur_trie:
            cur_trie[self.ind] = 0
        cur_trie[self.ind] += 1

    def search_k_leaf(self, k: int) -> bool:
        """
            search the existance of given word, in-order traverse with leaf node appearences greater than k
        """
        res = []

        def in_order(trie, path):
            # leaf node and appers>=k
            if self.ind in trie and trie[self.ind] == k:
                res.append(("".join(path), k))
            # a-z in trie
            for c in range(ord('a'), ord('a') + 27):
                c = chr(c)
                if c in trie:
                    in_order(trie[c], path + [c])

        in_order(self.trie, [])
        return res

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = TrieTree()
        for word in words:
            trie.insert(word)
        res = []
        n = len(words)
        while len(res) < k:
            res += trie.search_k_leaf(n)
            n -= 1

        return [x[0] for x in res[:k]]





