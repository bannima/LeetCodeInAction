#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i] 表示从第i位跳到最后一位所需要的最小步数
        dp = [0] * len(nums)
        for j in reversed(range(0,len(nums)-1)):
            dp[j] = min(dp[j+1:j+nums[j]+1]) +1 if nums[j]!=0 else float('inf')
        return dp[0]