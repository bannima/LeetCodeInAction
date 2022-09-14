#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

class MaxHeap():
    def __init__(self, ):
        self.arr = []

    def swap(self, i, j):
        tmp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = tmp

    def insert(self, val: int):
        self.arr.append(val)
        idx = len(self.arr) - 1
        while idx > 0 and self.arr[idx] > self.arr[(idx - 1) // 2]:
            self.swap(idx, (idx - 1) // 2)
            idx = (idx - 1) // 2

    def remove(self, ) -> int:
        if len(self.arr) == 0:
            return None
        elif len(self.arr) == 1:
            return self.arr.pop(0)
        val = self.arr[0]
        self.arr[0] = self.arr.pop(-1)
        idx = 0
        while idx < len(self.arr):
            left = idx * 2 + 1
            right = idx * 2 + 2
            # move left when left is both valid and greater than parent, and left is greater than right if right exists
            if left < len(self.arr) and self.arr[left] > self.arr[idx] and (
                    right >= len(self.arr) or self.arr[left] > self.arr[right]):
                self.swap(idx, left)
                idx = left
            elif right < len(self.arr) and self.arr[right] > self.arr[idx]:
                self.swap(idx, right)
                idx = right
            else:
                break
        return val


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MaxHeap()
        for n in nums:
            heap.insert(n)
        for _ in range(k):
            val = heap.remove()
        return val