#!/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-
from typing import List

class Node:
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next

    @classmethod
    def fromArray(cls, arr: List[int]):
        dh=Node(-1)
        cur=dh
        for num in arr:
            cur.next=Node(num)
            cur=cur.next
        return dh.next

    @classmethod
    def printList(cls,head):
        arr=[]
        cur=head
        while cur:
            arr.append(str(cur.value))
            cur=cur.next
        print("->".join(arr))


class Solution:
    def reverse(self, head: Node) -> Node:
        last=None
        cur,next=head,None
        while cur:
            next=cur.next
            cur.next=last
            last=cur
            cur=next
        return last

    def test(self):
        head=Node.fromArray([1,2,3])
        newHead=self.reverse(head)
        Node.printList(newHead)

if __name__ == '__main__':
    sol=Solution()
    sol.test()