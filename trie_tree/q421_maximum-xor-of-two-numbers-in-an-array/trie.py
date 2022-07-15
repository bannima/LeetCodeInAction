#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie.py
@time: 2022/7/15 11:09 PM
@desc: 
"""
from typing import List

class TrieTree():
    def __init__(self, ):
        self.trie = {}
        self.ind = "indices"

    def insert(self, word: str):
        cur_trie = self.trie
        for i, c in enumerate(word):
            if c not in cur_trie:
                cur_trie[c] = {}
            cur_trie = cur_trie[c]
        # end
        cur_trie[self.ind] = [word]

    def search(self, word: str):
        # 查找word是否存在于 字典数中
        cur_trie = self.trie
        for i, c in enumerate(word):
            if c not in cur_trie:
                return False
            cur_trie = cur_trie[c]
        return word in cur_trie[self.ind]

    def startswith(self, pref: str):
        # 查找字典树中是否存在前缀
        cur_trie = self.trie
        for i, c in enumerate(pref):
            if c not in cur_trie:
                return False
            cur_trie = cur_trie[c]
        return True

    def search_with_max_val(self, cur_trie, word, i):
        # 每次先查找 相反值的位置，这样高位异或结果越大，若没有，则用当前值，进行下一步
        if i == len(word):
            return cur_trie[self.ind][0]
        c = word[i]
        rev_c = '1' if c == '0' else '0'
        # print(cur_trie)
        if rev_c in cur_trie:
            return self.search_with_max_val(cur_trie[rev_c], word, i + 1)
        else:
            return self.search_with_max_val(cur_trie[c], word, i + 1)


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_value = float("-inf")
        trie = TrieTree()
        for i, n in enumerate(nums):
            # pad to 32 with left 0
            bi_n = bin(n)[2:].zfill(32)
            trie.insert(bi_n)
            # search tree with max num
            choosen_one = trie.search_with_max_val(trie.trie, bi_n, 0)
            max_value = max(max_value, int(choosen_one, 2) ^ n)
        return max_value





