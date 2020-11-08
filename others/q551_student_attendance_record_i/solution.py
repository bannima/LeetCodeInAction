#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/8 7:11 PM
Version: 0.1
"""
class Solution:
    def checkRecord(self, s: str) -> bool:
        isL = isA = 0
        for val in s:
            if val=='L':
                if isL<=2:
                    isL+=1
            elif val=='A':
                isA +=1
                isL = 0 if isL<=2 else isL
            else:
                isL = 0 if isL<=2 else isL

        if isL<=2 and isA<=1:
            return True
        else:
            return False

