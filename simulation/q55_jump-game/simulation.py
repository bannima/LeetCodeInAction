#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: simulation.py
@time: 2022/5/20 11:36 AM
@desc: 
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0 #表示i位置时，最远能跳到的位置数，跳跃游戏位置是连续的
        for i,n in enumerate(nums):
            if max_jump<i:
                return False
            max_jump = max(max_jump,n+i)
        return True