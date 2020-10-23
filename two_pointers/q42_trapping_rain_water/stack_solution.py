#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: stack_solution.py
Description: 
Author: Barry Chow
Date: 2020/10/23 8:58 PM
Version: 0.1
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        area = 0
        bottom = 0
        for i, h in enumerate(height):
            # empty stack
            if len(stack) == 0:
                stack.append(i)
            # 当前h比栈顶元素小，h入栈
            elif len(stack) > 0 and height[stack[-1]] > h:
                stack.append(i)
            # 栈顶元素出栈，计算增加的面积
            else:
                bottom = height[stack[-1]]
                while (len(stack) > 0) :
                    area += (min(height[stack[-1]], h)-bottom) * (i - stack[-1] - 1)
                    #area += (i - left - 1)
                    bottom = height[stack[-1]]

                    if height[stack[-1]] >= h:
                        break
                    stack.pop()

                stack.append(i)
        return area



