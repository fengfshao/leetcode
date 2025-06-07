#!/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def integer2str(self,num:int)->str:
        stk=[]
        while num!=0:
            ch=str(int(num%10))
            stk.append(ch)
            num=int(num/10)
        return ''.join(reversed(stk))


if __name__ == '__main__':
    sol = Solution()
    res = sol.integer2str(1234)
    print(res)
