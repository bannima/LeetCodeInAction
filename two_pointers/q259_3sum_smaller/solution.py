#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/7 10:23 AM
Version: 0.1
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums)<3:
            return 0
        #排序
        nums.sort()
        count = 0
        for s in range(len(nums)):
            #固定s，初始化为nums[s+1:len(nums)-1]两端的指针
            i,j = s+1,len(nums)-1
            while i<j:
                total = sum([nums[s],nums[i],nums[j]])
                #若当前和大于等于target，则表示需要减少和，即使右边最大的指针左移，j--
                if total>=target:
                    #和三数之和不同，这里要保存三元组位置的组合，所以即使相同元素但是位置不同，不能向前加速
                    #while(i<j and nums[j]==nums[j-1]): j-=1
                    j-=1
                #若当前和小于target，则表示对于目前的左指针i，有j-i个小于target和的方案，记录结果，跳过当前i
                else:
                    count+=(j-i)
                    i+=1

        return count


