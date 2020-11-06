#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: two_pointers.py
Description: 
Author: Barry Chow
Date: 2020/11/6 11:10 PM
Version: 0.1
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        排序+双指针+剪枝
        """
        if len(nums)<3:
            return []
        res=[]
        nums.sort()
        #对于每个s，都对nums[s+1:len(nums)-1]进行两端搜索找到和为0的组合
        for s in range(len(nums)):
            #表明s之后的元素都比nums[s]大，且nums[s]>0,肯定不会和为0，不用计算
            if(nums[s]>0):
                return res
            #组合相同，重复结果不用计算
            if(s>0 and nums[s]==nums[s-1]):
                continue

            i,j = s+1,len(nums)-1
            while(i<j):
                if nums[s]+nums[i]+nums[j]==0:
                    #不用担心重复结果在于下面两步排除了所有相同的结果
                    answer = [nums[s],nums[i],nums[j]]
                    res.append(answer)
                    while(i<j and nums[i]==nums[i+1]):
                        i+=1
                    while(i<j and nums[j]==nums[j-1]):
                        j-=1
                    i+=1
                    j-=1
                #和偏小，左指针i要右移，增加和
                elif nums[s]+nums[i]+nums[j]<0:
                    i+=1
                #和偏大，右指针j要左移，减少和
                else:
                    j-=1
        return res