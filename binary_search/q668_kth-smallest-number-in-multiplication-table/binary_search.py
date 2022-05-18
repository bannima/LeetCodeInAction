#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: binary_search.py
@time: 2022/5/18 11:30 AM
@desc: 
"""

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def nums_less_than_x(x):
            """ 统计乘法表中小于等于k的数字总和 """
            nums = [min(x//i,n) for i in range(1,m+1)]
            return sum(nums)
        l = 1
        r = m*n
        # 对于乘法表种所有可能的数字进行二分查找
        while l<r:
            mid = (l + r)>>1
            # 统计小于等于mid值的数字 个数
            count = nums_less_than_x(mid)
            # 若mid前面的数字个数，比k小，则扩大mid值，修改l
            if count<k:
                l= mid+1
            # 若mid前面的数字个数，大于或等于k，则缩小mid值，修改r
            else:
                r = mid
        return r

if __name__ == '__main__':
    m = 2
    n = 4
    k = 6
    ans = Solution().findKthNumber(m,n,k)
    print(ans)