#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: union_find.py
@time: 2022/5/3 3:59 PM
@desc: 
"""

from typing import List
from itertools import combinations

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_name = {}
        for account in accounts:
            name = account[0]
            mails = account[1:]
            for mail in mails:
                mail_name[mail] = name
        n = len(mail_name.keys())
        parents = list(range(n))
        # find parent
        def find(mail):
            i = list(mail_name.keys()).index(mail)
            while parents[i] != i:
                i = parents[i]
            return i
        # union op
        def union(mail_i,mail_j):
            parents[find(mail_i)] = find(mail_j)
        # merge
        for account in accounts:
            mails = account[1:]
            for edge in combinations(mails,2):
                union(edge[0],edge[1])

        # find all parents
        parent_ids = [find(list(mail_name.keys())[id]) for id in range(n)]
        print(parent_ids)
        res = []
        for parent_id in set(parent_ids):
            tmp = []
            parent_name = mail_name[list(mail_name.keys())[parent_id]]
            tmp.append(parent_name)
            # mail names
            parent_mails = [list(mail_name.keys())[id] for id in range(n) if parent_ids[id]==parent_id]
            # ascii order
            tmp += sorted(parent_mails)
            res.append(tmp)
        return res

if __name__ == '__main__':
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    res = Solution().accountsMerge(accounts=accounts)
    print(res)