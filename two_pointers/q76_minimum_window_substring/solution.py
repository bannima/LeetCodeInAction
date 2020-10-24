#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: solution.py
Description: 
Author: Barry Chow
Date: 2020/10/24 2:58 PM
Version: 0.1
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        双指针法
        :type s: str
        :type t: str
        :rtype: str
        """
        # 结果
        min_length = len(s) + 1
        begin = len(s)
        end = -1

        # 用子串的字符频率来唯一的标识该子串
        t_dict = {}
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        # 正确的子串频率标识

        left = 0
        pos = 0
        hash_map = {}
        while pos < len(s):
            # 若left：pos不包含t的所有子串，则不断加入元素
            if not self.contain_dict(hash_map, t_dict):
                # 只关心在t中的字符的频率
                if s[pos] in t_dict:
                    if s[pos] in hash_map:
                        hash_map[s[pos]] += 1
                    else:
                        hash_map[s[pos]] = 1

                # 若left：pos包含t的所有字符，则不断left++，一定要保持包含子串性质，
                # 记录结果,直到不包含子串的性质
                while (self.contain_dict(hash_map, t_dict)):
                    # 记录结果
                    if (pos - left + 1) < min_length:
                        min_length = pos - left + 1
                        begin = left
                        end = pos

                    if s[left] in t_dict:
                        if s[left] in hash_map:
                            hash_map[s[left]] -= 1
                        else:
                            break
                    left += 1
                pos += 1

        return s[begin:end + 1]

    def contain_dict(self, query, answer):
        '''
        比较两个子串中的频率数据，确保所有query的频率均小于answer的频率，即query包含answer返回True
        '''

        if len(query.values()) < len(answer.values()):
            return False
        '''
        for a,b in zip(query.values(),answer.values()):
            if a<b:
                return False
        '''
        for key, value in answer.items():
            if query[key] < value:
                return False

        return True