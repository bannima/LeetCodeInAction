#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie_oot.py
@time: 2022/7/16 5:29 PM
@desc: 
"""
from typing import List

class TrieTree():
    def __init__(self, ):
        self.trie = {}
        self.leaf = "is_leaf"

    def insert(self, word: str):
        cur_trie = self.trie
        for i, c in enumerate(word):
            if c not in cur_trie:
                cur_trie[c] = {}
            cur_trie = cur_trie[c]
        cur_trie[self.leaf] = True

    def search(self, word: str):
        cur_trie = self.trie
        for i, c in enumerate(word):
            if c not in cur_trie:
                return False
            cur_trie = cur_trie[c]

        return self.leaf in cur_trie and cur_trie[self.leaf]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False] * n for _ in range(m)]
        self.trie = TrieTree()
        self.dfs = []

        def legal_pos(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        def dfs(i, j, word):
            if len(word) > 10:
                return
                # save word info in trie
            if word not in self.dfs:
                self.trie.insert(word)
                self.dfs.append(word)
            for dir in dirs:
                ni, nj = i + dir[0], j + dir[1]
                if legal_pos(ni, nj) and not visited[ni][nj]:
                    visited[ni][nj] = True
                    dfs(ni, nj, word + board[ni][nj])
                    visited[ni][nj] = False

        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                dfs(i, j, board[i][j])
                visited[i][j] = False

        ans = []
        for word in set(words):
            # preprocess for judge existance
            if self.trie.search(word):
                ans.append(word)
        return ans




