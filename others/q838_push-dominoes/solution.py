#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/2/26 10:06 PM
@desc: 
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        def look_left(i, dominoes):
            init = i
            while (i >=0):
                if dominoes[i] == '.':
                    i -= 1
                elif dominoes[i] == 'L':
                    return -1
                else:  # R
                    return init - i
            return -1

        def look_right(i, dominoes):
            init = i
            while (i < len(dominoes)):
                if dominoes[i] == '.':
                    i += 1
                elif dominoes[i] == 'R':
                    return -1
                else:  # L
                    return i - init
            return -1

        res = []
        # 对于每个点，只要计算其左右两边往这里传到的力谁更近即可
        for i in range(len(dominoes)):
            # 跳过发力点
            if dominoes[i] != '.':
                res.append(dominoes[i])
                continue
            # 找到最左边第一个发力点是否为往右，若往右，其传递距离；若不往右，返回-1
            left = look_left(i-1, dominoes)
            # 找到最右边第一个发力点是否为往左，若往左，其传递距离，若不往左，返回-1
            right = look_right(i+1, dominoes)
            # 比较两个力谁更近，若相等则表示.
            if left != -1 and right != -1:
                if left > right:
                    res.append('L')
                elif left < right:
                    res.append('R')
                else:
                    res.append('.')
            elif left == -1 and right == -1:
                res.append('.')

            elif left == -1 and right != -1:
                res.append('L')

            else:
                res.append('R')
        return ''.join(res)

if __name__ =='__main__':
    s = Solution()
    res = s.pushDominoes(dominoes="R.")
    assert res=="RR"
