#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description:
Author: Barry Chow
Date: 2021/3/23 5:08 PM
Version: 0.1
"""


# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def dfs(self, nested):
        for v in nested:
            if v.isInteger():
                self.elements.append(v.getInteger())
            else:
                self.dfs(v.getList())

    def __init__(self, nestedList: [NestedInteger]):
        self.elements = []
        self.dfs(nestedList)

    def next(self) -> int:
        return self.elements.pop(0)

    def hasNext(self) -> bool:
        return len(self.elements) > 0