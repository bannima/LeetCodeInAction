#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MaxHeap():
    # 最大堆
    def __init__(self, ):
        self.array = []

    def swap(self, i, j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    def add_element(self, val: int):
        # 向最大堆中添加元素
        # 具体实现为尾部增加元素，并自底向上遍历父节点，若比父节点大直接交换
        self.array.append(val)
        idx = len(self.array) - 1
        while idx >= 0:
            parent_id = idx // 2
            if self.array[parent_id] < self.array[idx]:
                # swap with parent
                self.swap(idx, parent_id)
                # up
                idx = parent_id
            else:
                break

    def remove_top(self, ) -> str:
        # 向最大堆中删除元素
        # 具体实现为 删除堆顶元素，将最大堆的末尾元素覆盖到堆顶，并自顶向下遍历交换元素
        if len(self.array) == 0:
            return None
        elif len(self.array) == 1:
            return self.array[0]
        val = self.array[0]
        self.array[0] = self.array.pop(-1)

        idx = 0
        while idx < len(self.array):
            left_idx = idx * 2 + 1
            right_idx = idx * 2 + 1
            if left_idx<len(self.array) and self.array[idx] < self.array[left_idx]:
                self.swap(idx, left_idx)
                idx = left_idx
            elif right_idx<len(self.array) and self.array[idx] < self.array[right_idx]:
                self.swap(idx, right_idx)
                idx = right_idx
            else:
                break
        return val

if __name__ == '__main__':
    heap = MaxHeap()
    for val in [1,32,32,2,3,49,9,87,13]:
        heap.add_element(val)
    k=3
    for i in range(k):
        print(heap.remove_top())