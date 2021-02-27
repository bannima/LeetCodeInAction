
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
FileName: binary.py
Description: 
Author: Barry Chow
Date: 2021/2/27 8:16 PM
Version: 0.1
"""


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while (l <= r):
            mid = (l + r) // 2

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid - 1]:
                r = mid - 1
            elif arr[mid] < arr[mid + 1]:
                l = mid + 1

        return -1
