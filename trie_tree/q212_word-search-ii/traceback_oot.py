#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: traceback_oot.py
@time: 2022/7/16 4:53 PM
@desc: out of time solution with traceback

"""

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        words_set = set(words)
        ans = []
        # visited flag
        visited = [[False] * n for _ in range(m)]

        def legal_pos(i, j):
            return i < m and i >= 0 and j < n and j >= 0

        def dfs(i, j, word):
            if len(word) > 10:
                return
            if word in words_set:
                ans.append(word)
                words_set.remove(word)
            for dir in dirs:
                ni, nj = i + dir[0], j + dir[1]
                if legal_pos(ni, nj) and visited[ni][nj] == False:
                    visited[ni][nj] = True
                    dfs(ni, nj, word + board[ni][nj])
                    visited[ni][nj] = False

        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                dfs(i, j, board[i][j])
                visited[i][j] = False
        return ans








