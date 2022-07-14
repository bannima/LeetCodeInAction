#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: stack_method.py
@time: 2022/7/14 10:24 AM
@desc: 
"""


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True
            while alive and stack and ast<0 and stack[-1]>0:
                alive = stack[-1]<abs(ast)
                if stack[-1]<=abs(ast):
                    stack.pop(-1)
            if alive:
                stack.append(ast)
        return stack


