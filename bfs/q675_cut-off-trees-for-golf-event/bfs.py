#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs.py
@time: 2022/5/23 10:49 AM
@desc: 
"""

from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if forest[0][0] == 0: return -1
        m, n = len(forest), len(forest[0])
        dirs = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        # 所有要砍伐掉树木的高度，数量
        total_tree = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    total_tree.append((forest[i][j], i, j))

        total_tree.sort(key=lambda x: x[0])
        print(total_tree)

        def legal_pos(ni, nj):
            if (ni >= 0 and ni < m) and (nj >= 0 and nj < n):
                return True
            return False

        def bfs(si, sj, ti, tj):
            """从i，j出发，找到ti,tj位置的最短步数"""
            # 比较是否找到了所有的树，若是则记录步骤数
            visited = set()
            visited.add((si, sj))
            path = [(si, sj)]
            steps = 0
            while path:
                next_path = []
                for i,j in path:
                    if i == ti and j == tj:
                        return steps
                    for dir in dirs:
                        ni, nj = i + dir[0], j + dir[1]
                        # 下一位置合法，且不为零，且升序,且没有访问过
                        if legal_pos(ni, nj) and forest[ni][nj] != 0 and ((ni, nj) not in visited) :
                            # 记录路径，和所砍掉的树高度,dfs查找
                            next_path.append((ni, nj))
                            visited.add((ni, nj))
                path = next_path
                steps += 1
            return -1

        total_steps = 0
        si, sj = 0, 0
        for _, ti, tj in total_tree:
            step = bfs(si, sj, ti, tj)
            if step == -1: return -1
            total_steps += step
            si, sj = ti, tj

        return total_steps


if __name__ == '__main__':
    forest = [[1,2,0],
              [0,3,4],
              [7,6,5]]
    # forest = [[54581641,64080174,24346381,69107959],
    #           [86374198,61363882,68783324,79706116],
    #           [668150,92178815,89819108,94701471],
    #           [83920491,22724204,46281641,47531096],
    #           [89078499,18904913,25462145,60813308]]
    res = Solution().cutOffTree(forest)
    print(res)


