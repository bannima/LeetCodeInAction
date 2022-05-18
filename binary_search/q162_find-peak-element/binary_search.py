#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: binary_search.py
@time: 2022/5/18 8:51 PM
@desc: 
"""
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        为什么二分查找大的那一半一定会有峰值呢？（即nums[mid]<nums[mid+1]时，mid+1~N一定存在峰值）
        我的理解是，首先已知 nums[mid+1]>nums[mid]，那么mid+2只有两种可能，
        一个是大于mid+1，一个是小于mid+1，小于mid+1的情况，那么mid+1就是峰值，
        大于mid+1的情况，继续向右推，如果一直到数组的末尾都是大于的，那么可以肯定最后一个元素是峰值
        ，因为nums[nums.length]=负无穷
        """
        l,r = 0,len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m]<nums[m+1]:
                l= m+1
            else:
                r = m
        return r