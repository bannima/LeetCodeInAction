#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: backtrace.py
Description: 
Author: Barry Chow
Date: 2021/3/22 5:45 PM
Version: 0.1
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def legal_ip(ip):
            num = int(ip)
            if num<=255 and num>=0:
                if len(ip)>1 and ip[0]!='0':
                    return True
                elif len(ip)==1:
                    return True
            return False

        def find(path,depth,remain):
            if depth==4 and len(remain)==0:
                path = ".".join(path)
                res.append(path)
                return
            elif depth>4:
                return

            for i in range(1,len(remain)+1):
                if legal_ip(remain[:i]):
                    find(path+[remain[:i]],depth+1,remain[i:])
        find([],0,s)
        return res