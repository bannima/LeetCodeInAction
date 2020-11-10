#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/11/10 12:28 PM
Version: 0.1
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        从后往前遍历，找到第一个大于前一个数字的序号n，在此基础上，从n往后遍历，
        记录下比n-1位置大但尽可能小的数，将这个数和n-1交换，
        并将n及以后的数字进行升序排序，这样得到的结果最小
        """

        def reverse(i, j):
            # reverse nums from i to j,nums[i:j]
            while (i < j):
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1;
                j -= 1

        if len(nums) <= 1:
            return nums
        i = len(nums) - 2;
        j = len(nums) - 1

        # 找到从nums[i+1:j]中比nums[i]大的所有值中最小值,即对应的j和i
        flag = False
        while (i >= 0 and j > i):
            while (j > i):
                if nums[j] <= nums[i]:
                    j -= 1
                else:
                    flag = True
                    break
            if flag:
                break
            else:
                j = len(nums) - 1
                i -= 1
        if i == -1:
            reverse(0, len(nums) - 1)
        else:
            # 此时nums[i]<nums[j]
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            reverse(i + 1, len(nums) - 1)
