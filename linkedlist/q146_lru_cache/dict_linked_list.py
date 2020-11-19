#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: dict_linked_list.py
Description: 
Author: Barry Chow
Date: 2020/11/19 8:11 PM
Version: 0.1
"""


class Node:
    def __init__(self, key, x):
        self.key = key
        self.val = x
        self.next = None
        self.previous = None


class LRUCache:
    '''
    链表尾部为最新使用的元素，链表头部为最久未使用元素
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = None
        self.cur = None

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            node = self.dic[key]
            x = node.val
            if self.head == self.cur:
                return x
            elif self.head == node:
                node.next.previous = None
                self.head = self.head.next
            elif node == self.cur:
                return x
            else:
                node.previous.next = node.next
                node.next.previous = node.previous

            self.cur.next = node
            node.previous = self.cur
            self.cur = self.cur.next
            return x

    def put(self, key: int, value: int) -> None:
        if len(self.dic) == 0:
            node = Node(key, value)
            self.head = self.cur = node
            self.dic[key] = node

        elif key not in self.dic:
            if len(self.dic) < self.capacity:
                # 插入元素
                self.cur.next = Node(key, value)
                self.cur.next.previous = self.cur
                self.cur = self.cur.next

                self.dic[key] = self.cur
            # cache满，删除元素,再插入
            else:
                del self.dic[self.head.key]

                # 元素清空
                # 若不止一个元素
                if self.head != self.cur:
                    self.head = self.head.next
                    # 插入元素
                    self.cur.next = Node(key, value)
                    self.cur.next.previous = self.cur
                    self.cur = self.cur.next
                    self.dic[key] = self.cur
                # 若只有一个元素
                elif self.head == self.cur:
                    self.cur.next = Node(key, value)
                    self.cur.next.previous = self.cur
                    self.cur = self.cur.next
                    self.dic[key] = self.cur
                    self.head = self.cur

        # 在链表中，则更新元素值，同时将node移动到链表尾，
        else:
            node = self.dic[key]
            node.val = value
            if self.head == self.cur:
                return

            elif self.head == node:
                self.head = self.head.next
                self.cur.next = node
                node.previous = self.cur
                self.cur = self.cur.next

            elif node == self.cur:
                return
            else:
                node.previous.next = node.next
                node.next.previous = node.previous
                self.cur.next = node
                node.previous = self.cur
                self.cur = self.cur.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)