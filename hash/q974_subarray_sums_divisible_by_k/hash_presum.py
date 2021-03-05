#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: hash_presum.py
Description: 
Author: Barry Chow
Date: 2021/3/5 5:58 PM
Version: 0.1
"""


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dic = {0: 1}
        pre = 0
        count = 0

        for i in range(len(A)):
            pre = (pre + A[i]) % K

            if pre in dic:
                count += dic[pre]
                dic[pre] += 1
            else:
                dic[pre] = 1
        return count

