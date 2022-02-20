#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/2/20 4:43 PM
@desc: 
"""


class Solution:
    def isOneBitCharacter(self, bits) -> bool:
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                if i == len(bits) - 1:  # last i
                    return True
            if bits[i] == 1:
                i += 1  # skip next value after '1'
            i += 1

        return False

if __name__ == '__main__':
    s = Solution()
    res = s.isOneBitCharacter([1,0,0])
    assert res==True
