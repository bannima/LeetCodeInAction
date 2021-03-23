#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution2.py
Description: 
Author: Barry Chow
Date: 2021/3/23 6:37 PM
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
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            cur = self.stack.pop()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])
        return False