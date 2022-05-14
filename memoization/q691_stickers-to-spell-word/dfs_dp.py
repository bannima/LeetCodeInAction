#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@version: 0.1
@author: zhouenguo
@license: Apache Licence
@file: dfs_dp.py
@time: 2022/5/14 11:41 PM
@desc: 
"""
from typing import List

class Str2Array():
    """
    save string to 26 bit array, and define mins, add ops
    """
    def __init__(self, s):
        self.array = {}
        for c in s:
            if c not in self.array:
                self.array[c]=0
            self.array[c] += 1
    def mins(self, s2):
        """
        s1 - s2 can be regarded as differ op in set
        """
        target_s = Str2Array("")
        for c in self.array:
            # c are common char in both self and s2
            t = self.array[c] - s2.array.get(c,0)
            if t>0:
                target_s.array[c] = t
        return target_s
    def contains(self, s2) -> bool:
        return len(set(list(self.array.keys())) & set(list(s2.array.keys())))
    def is_null(self):
        return sum(list(self.array.values())) == 0
    def to_str(self):
        s_id = ""
        for c,v in self.array.items():
            s_id += "{}{}".format(c,v)
        return s_id

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target = Str2Array(target)
        stickers = [Str2Array(s) for s in stickers]
        times = {}
        def dfs(target):
            """找到当前target所需要的最小的次数"""
            if target.is_null():
                return 0
            elif target.to_str() in times:
                return times[target.to_str()]
            min_times = float("inf")
            for s in stickers:
                # 包含共同部分，需要找
                if target.contains(s):
                    min_times = min(min_times, dfs(target.mins(s)) + 1)
            times[target.to_str()] = min_times
            return min_times

        ans = dfs(target)
        return ans if ans != float("inf") else -1


if __name__ == '__main__':
    # stickers = ["with", "example", "science"]
    # target = "thehat"
    stickers = ["gone","dont","bell","simple","colony","mine","carry","sleep","village","ready","ground","sell","use","lead","doctor","stretch","less","except","long","why","indicate","live","animal","blow","inch","got","include","hope","real","then","string","degree","syllable","blue","stop","job","key","class","he","valley","did","country","space","heat","collect","truck","mother","problem","toward","my"]
    target = "bringmethod"
    res = Solution().minStickers(stickers,target)
    print(res)




