#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: bfs.py
@time: 2022/5/8 3:58 PM
@desc: 
"""
from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = []
        queue.append((start, 0))
        visited = {}
        min_step = float("inf")
        while queue:
            s, step = queue.pop(0)
            if s == end:
                min_step = min(min_step, step)
            for i in range(8):
                for c in ['A', 'C', 'G', 'T']:
                    if s[i] != c:
                        # generate next s
                        next_s = list(s)
                        next_s[i] = c
                        next_s = "".join(next_s)
                        # if next s in bank
                        if next_s in bank:
                            # not visited
                            if next_s not in visited:
                                visited[next_s] = step + 1
                                queue.append((next_s, step + 1))
                            # visited

        return min_step if min_step != float("inf") else -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        self.min_step = float("inf")
        visited = {}

        def bfs(s, step):
            if s == end:
                self.min_step = min(self.min_step, step)
            for i in range(8):
                for c in list('ACGT'):
                    if s[i] != c:
                        next_s = list(s)
                        next_s[i] = c
                        next_s = "".join(next_s)
                        if next_s in bank and next_s not in visited:
                            visited[next_s] = step
                            bfs(next_s, step + 1)

        bfs(start, 0)
        return self.min_step if self.min_step != float("inf") else -1
