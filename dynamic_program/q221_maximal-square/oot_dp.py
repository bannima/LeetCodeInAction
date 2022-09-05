#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        dp = [[0] * n for _ in range(m)]
        for l in range(1, min(m, n) + 1):
            for i in range(l - 1, m):
                for j in range(l - 1, n):
                    if l == 1:
                        dp[i][j] = 1 if matrix[i][j] == '1' else 0
                        max_area = max(max_area, dp[i][j])
                    else:
                        # 向左上角遍历一次得到，左上角以上的部分是否为正方形, 且以(i,j)为终点的两条长为l的边全是1，
                        if matrix[i][j] == '1' and dp[i - 1][j - 1] in [ (l-1)**2,l**2]:
                            if sum([int(v) for v in matrix[i][j - l+1:j+1]]) == l and sum(
                                    [int(matrix[k][j]) for k in range(i - l+1, i+1)]) == l:
                                dp[i][j] = l ** 2
                                max_area = max(max_area, dp[i][j])

        return max_area


if __name__ == '__main__':

    #matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    #matrix = [["1","1"],["1","1"]]
    matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
    res = Solution().maximalSquare(matrix)
    print(res)

