#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2021/3/5 3:09 PM
Version: 0.1
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, v):
        self.stack.append(v)

    def peek(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            return None

    def pop(self):
        if len(self.stack):
            v = self.stack[-1]
            self.stack.pop()
            return v
        else:
            return None

    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l_stack = Stack()
        self.r_stack = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.r_stack.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self._transform()
        # 左栈元素在出栈
        return self.l_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._transform()
        return self.l_stack.peek()

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.l_stack.empty() and self.r_stack.empty

    def _transform(self):
        if self.l_stack.size() == 0:
            # 左右栈元素互换
            while (self.r_stack.size()):
                self.l_stack.push(self.r_stack.pop())
