#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: trie.py
@time: 2022/7/16 5:59 PM
@desc: 
"""




class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.leaf = "leaf"


    def insert(self, key: str, val: int) -> None:
        cur_trie = self.trie
        for i,c in enumerate(key):
            if c not in cur_trie:
                cur_trie[c] = {}
            cur_trie = cur_trie[c]
        # set val
        cur_trie[self.leaf] = val

    def sum(self, prefix: str) -> int:
        #print(self.trie)
        cur_trie = self.trie
        for i,c in enumerate(prefix):
            if c not in cur_trie:
                return 0
            cur_trie = cur_trie[c]
        # locate the cur trie level, where leaf nodes in cur tries startswith same prefix
        self.s = 0
        def dfs(cur_trie):
            #print(cur_trie)
            if self.leaf in cur_trie:
                self.s += cur_trie[self.leaf]
            for c in cur_trie:
                if c!=self.leaf:
                    dfs(cur_trie[c])
        dfs(cur_trie)
        return self.s



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
