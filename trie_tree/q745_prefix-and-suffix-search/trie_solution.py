#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie_solution.py
@time: 2022/7/14 10:02 AM
@desc:
"""

from typing import List

class TrieTree():
    def __init__(self, words: List[str]):
        # 初始化字典树
        self.trie = {}
        self.insert_words(words)

    def insert_words(self, words: List[str]):
        # id 表示单词的位置
        for id, word in enumerate(words):
            self.insert(word, id)

    def insert(self, word: str, id):
        cur_trie = self.trie
        for i, c in enumerate(word):
            if c not in cur_trie:
                cur_trie[c] = {}
            cur_trie = cur_trie[c]
            if 'idx' not in cur_trie:
                cur_trie['idx'] = []
            cur_trie['idx'].append(id)
        # i== len(word)-1
        cur_trie['leaf'] = True

    def search(self, word: str) -> bool:
        # 查找字典树
        cur_trie = self.trie
        for i, c in enumerate(word):
            if c not in cur_trie:
                return False
            cur_trie = cur_trie[c]
        # 判断是否为包含该字符串的叶子节点
        if 'leaf' in cur_trie:
            return True
        return False

    def search_prefix_nodes(self, prefix: str) -> List:
        # 查找字典树
        cur_trie = self.trie
        for i, c in enumerate(prefix):
            if c not in cur_trie:
                return []
            cur_trie = cur_trie[c]
        return cur_trie.get('idx', [])


class WordFilter:
    def __init__(self, words: List[str]):
        self.pref_trie_tree = TrieTree(words)
        words_re = [word[::-1] for word in words]
        self.suff_trie_tree = TrieTree(words_re)
    # 重复值
    @cache
    def f(self, pref: str, suff: str) -> int:
        pref_idx = self.pref_trie_tree.search_prefix_nodes(pref)
        suff_idx = self.suff_trie_tree.search_prefix_nodes(suff[::-1])
        inter_ids = list(set(pref_idx) & set(suff_idx))
        return max(inter_ids) if len(inter_ids) else -1
