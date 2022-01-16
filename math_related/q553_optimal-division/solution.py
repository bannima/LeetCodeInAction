
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: solution.py
@time: 2022/1/16 10:47 AM
@desc: 
"""


class Solution:
    def optimalDivision(self, nums):
        # if len(nums)==1:
        #     return ''.join([str(n) for n in nums])
        res = []
        for n in nums:
            res.append(str(n))
            res.append('/')
        res.pop()#
        if len(res)>3:
            res.insert(2,'(')
            res.append(')')
        return ''.join(res)