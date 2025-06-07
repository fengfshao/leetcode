#!/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
class Frame:
    a, b, pc = 0, 0, 0

    def __init__(self, n):
        self.n = n


class Solution:
    def fibonaci(self, n: int) -> int:
        if n < 3:
            return 1
        a = self.fibonaci(n - 1)
        b = self.fibonaci(n - 2)
        return a + b

    def fibonaci2(self, n: int) -> int:
        """
        将递归用栈来模拟实现
        :param n:
        :return:
        """
        stk, ret = [], 0
        stk.append(Frame(n))

        def _fibonaci2():
            nonlocal stk, ret
            while stk:
                frame = stk[len(stk) - 1]
                if frame.pc == 0:
                    frame.pc = 1
                    if frame.n < 3:
                        ret = 1
                        stk.pop()
                        continue
                    stk.append(Frame(frame.n - 1))
                    continue
                elif frame.pc == 1:
                    frame.pc = 2
                    frame.a = ret
                    stk.append(Frame(frame.n - 2))
                    continue
                else:
                    frame.b = ret
                    ret = frame.a + frame.b
                    stk.pop()

        _fibonaci2()
        print(len(stk))
        return ret


if __name__ == '__main__':
    sol = Solution()
    print(sol.fibonaci2(9))
