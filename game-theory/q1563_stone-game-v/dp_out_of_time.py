#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dp.py
@time: 2022/5/25 2:39 PM
@desc: 
"""

from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        # dp[i][j] 表示在剩余 s[i:j]时(j为闭区间)，alice能够获得的最大分数
        self.dp = {}

        # 定义前缀和，减少计算时间,pre_sum[i]表示到i（含i）的位置，所有数组的和
        pre_sum = []
        cur_sum = 0
        for i in range(n):
            cur_sum += stoneValue[i]
            pre_sum.append(cur_sum)

        # print(pre_sum)

        # 返回区间为[i,j]时，j为闭区间，能够得到的最大分数
        def dfs(i, j):
            # 表示区间长度（j-i+1）为1，游戏结束
            if (i, j) not in self.dp:
                if j == i:
                    best = 0
                else:
                    best = float("-inf")
                    # 对于s种分割位置
                    for s in range(1, j - i + 1):
                        # 左边比较大，丢弃左边，保留右边
                        if (pre_sum[i + s - 1] - pre_sum[i] + stoneValue[i]) > (
                                pre_sum[j] - pre_sum[i + s] + stoneValue[i + s]):
                            # if sum(stoneValue[i:i + s]) > sum(stoneValue[i + s:j + 1]):
                            ans = sum(stoneValue[i + s:j + 1]) + dfs(i + s, j)
                        # 右边比较大，丢弃右边,保留左边
                        elif (pre_sum[i + s - 1] - pre_sum[i] + stoneValue[i]) < (
                                pre_sum[j] - pre_sum[i + s] + stoneValue[i + s]):
                            # elif sum(stoneValue[i:i + s]) < sum(stoneValue[i + s:j + 1]):
                            ans = dfs(i, i + s - 1) + sum(stoneValue[i:i + s])
                        # 两边相等,两种情况都考虑，选择最大的对alice最有利
                        else:
                            ans1 = (pre_sum[j] - pre_sum[i + s] + stoneValue[i + s]) + dfs(i + s, j)
                            ans2 = dfs(i, i + s - 1) + (pre_sum[i + s - 1] - pre_sum[i] + stoneValue[i])
                            ans = max(ans1, ans2)
                        best = max(best, ans)
                self.dp[(i, j)] = best
            return self.dp[(i, j)]

        ans = dfs(0, n - 1)
        return ans

if __name__ == '__main__':

    #stoneValue = [6,2,3,4,5,5]
    stoneValue = [2,1,1]

    ans = Solution().stoneGameV(stoneValue)
    print(ans)



