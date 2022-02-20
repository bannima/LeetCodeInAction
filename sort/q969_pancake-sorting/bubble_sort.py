#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: bubble_sort.py
@time: 2022/2/20 5:15 PM
@desc: 
"""

class Solution:
    def pancakeSort(self, arr):
        #panca sort arr[0:i+1]
        def inplace_reverse(l,r):
            '''reverse the arr[l:r] based on pancakasort'''
            while l<r:
                tmp = arr[l]
                arr[l] = arr[r]
                arr[r] = tmp
                l+=1
                r-=1
        def panca(i):
            max_p = 0
            max_v = arr[0]
            #find the max value index
            for j in range(i+1):
                if arr[j]>max_v:
                    max_v = arr[j]
                    max_p = j
            #reorder the arr in new order
            inplace_reverse(0,max_p)
            inplace_reverse(0,i)
            return [max_p+1,i+1]
        k_list =[]
        for i in reversed(range(1,len(arr))):
            k_list += panca(i)
        return k_list

if __name__ =='__main__':
    s = Solution()
    res = s.pancakeSort([3,2,4,1])
    print(res)
