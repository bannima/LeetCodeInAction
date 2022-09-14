#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


class Pair():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


class MaxHeap():
    # 最大堆
    def __init__(self, ):
        self.array = []

    def swap(self, i, j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    def add(self, pair: Pair):
        # 向最大堆中添加元素
        # 具体实现为尾部增加元素，并自底向上遍历父节点，若比父节点大直接交换
        self.array.append(pair)
        idx = len(self.array) - 1
        while idx >= 0 and ((idx - 1) // 2)>=0 and self.array[(idx - 1) // 2] < self.array[idx]:
            # swap with parent
            self.swap(idx, (idx - 1) // 2)
            # up
            idx = (idx - 1) // 2

    def remove(self, ) -> Pair:
        # 向最大堆中删除元素
        # 具体实现为 删除堆顶元素，将最大堆的末尾元素覆盖到堆顶，并自顶向下遍历交换元素,每向下一步，考虑左右子树的更大直
        if len(self.array) == 0:
            return None
        elif len(self.array) == 1:
            return self.array.pop()
        # len(array)>=2 condition:
        val = self.array[0]
        self.array[0] = self.array.pop(-1)
        idx = 0
        while idx < len(self.array):
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 2
            # 确保左分支有效，若右分支存在，必须比右边分支更大
            if left_idx < len(self.array) and self.array[idx] < self.array[left_idx] and (right_idx >= len(self.array) or self.array[left_idx]>self.array[right_idx]):
                self.swap(idx, left_idx)
                idx = left_idx
            elif right_idx < len(self.array) and self.array[idx] < self.array[right_idx]:
                self.swap(idx, right_idx)
                idx = right_idx
            else:
                break
        return val


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        heap = MaxHeap()
        for val, times in counter.items():
            pair = Pair(val, times)
            heap.add(pair)
        res = []
        for _ in range(k):
            val = heap.remove()
            res.append(val.key)
        return res


if __name__ == '__main__':
    # nums = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5]
    # k = 7
    nums = [3,0,1,0]
    k=1
    s = Solution().topKFrequent(nums,k)
    print(s)
