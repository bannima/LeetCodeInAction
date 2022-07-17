#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: simulation.py
@time: 2022/7/17 4:33 PM
@desc: 
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        # 右 下 左 上
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        # 逐层打印
        for i in range(min((n + 1) // 2,(m+1)//2)):
            # 每一层，固定起始位置
            pos_i,pos_j = i,i

            # 计算当前层矩阵的横向步数，纵向步数
            m_step = m - i * 2 - 1
            n_step = n - i * 2 -1

            # 当前层，四个方向，遍历length步，打印结果
            for id,dir in enumerate(dirs):
                # 走固定步数,看是什么方向
                cur_step = m_step if id%2==1 else n_step
                for s in range(cur_step):
                    # 输出结果
                    ans.append(matrix[pos_i][pos_j])

                    pos_i,pos_j = pos_i+dir[0],pos_j+ dir[1]
        ans.append(matrix[pos_i][pos_j])
        return ans[:m*n]





if __name__ == "__main__":
    #matrix = [[1,2,3],[4,5,6],[7,8,9]]
    #matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    matrix = [[6,9,7]]
    res = Solution().spiralOrder(matrix)
    print(res)

