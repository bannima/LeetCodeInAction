#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
            回溯+剪枝，剪枝条件为任意有效的括号，在任何位置截断时候，左括号的个数都小于等于右括号的个数
        """
        ans = []
        def backtrace(path,left,right):
            if len(path)==2*n:
                ans.append("".join(path))
            if left<n:
                backtrace(path+['('],left+1,right)
            if right<left:
                backtrace(path+[')'],left,right+1)
        backtrace([],0,0)
        return ans