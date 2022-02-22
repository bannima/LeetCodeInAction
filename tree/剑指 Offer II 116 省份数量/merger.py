#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: merger.py
@time: 2022/2/21 9:19 PM
@desc: 
"""
class Solution:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        prov = list(range(1,n+1))
        prov = [-1 * val for val in prov]
        print(prov)
        print(max(prov))
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]==1: # (i,j,edge)
                    #merge i's prov and j's prov
                    next_prov = max(prov) + 1
                    #case 1: init
                    if prov[i]<0 and prov[j]<0:
                        prov[i]=next_prov
                        prov[j]=next_prov
                    elif prov[i]<0:
                        prov[i] = prov[j]
                    elif prov[j]<0:
                        prov[j] = prov[i]
                    elif prov[i]==prov[j]:
                        continue
                    #case 5: merge two group provs
                    else:
                        for k,prov_val in enumerate(prov):
                            if prov_val == prov[i]:
                                prov[k] = prov[j]
        return len(set(prov))


if __name__ =='__main__':
    s = Solution()
    res = s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
    print(res)

