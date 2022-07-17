#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: simulation.py
@time: 2022/7/17 3:28 PM
@desc: 
"""
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        board = [[0] * n for _ in range(n)]
        # 右，下，左，上 顺序不能乱
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cnt = 1
        # 逐层次遍历，填充元素
        for i in range((n + 1) // 2):
            length = n - 1 - 2*i
            # start pos
            pos_i, pos_j = i, i
            board[pos_i][pos_j] = cnt
            # cnt +=1
            # 每一层，逐个打印值,具体为每个方向，走length步骤
            for dir in dirs:
                for l in range(length):
                    board[pos_i][pos_j] = cnt
                    cnt += 1
                    # 新的位置
                    pos_i, pos_j = pos_i + dir[0], pos_j + dir[1]
        return board

if __name__ == "__main__":
    res = Solution().generateMatrix(n=3)
    print(res)

