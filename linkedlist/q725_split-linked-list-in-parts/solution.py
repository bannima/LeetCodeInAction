#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/9/22 8:50 PM
Version: 0.1
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        def get_length(root):
            '''返回列表的长度'''
            if root is None:
                return 0
            count = 1
            while (root.next):
                count += 1
                root = root.next
            return count

        def get_split(n, k):
            '''将长度为n的数组，切分k份'''
            res = []
            share = n // k
            for i in range(k):
                res.append(share)
            # 剩余的补充1
            for j in range(n % k):
                res[j] = res[j] + 1
            return res

        split_list = []
        length = get_length(head)

        splits = get_split(length, k)
        print(splits)

        for part in range(k):
            if splits[part] == 0:
                split_list.append(None)
            else:
                split_list.append(head)
                print("## ", split_list)

                for j in range(splits[part]):
                    if j == (splits[part] - 1):  # last step
                        root = head.next
                        print(j)
                        head.next = None
                        print('#head ', head)
                        print('#root ', root)
                    head = head.next
                head = root
        return split_list






