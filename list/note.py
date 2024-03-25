from solution import ListNode
from typing import Optional

'''
逆序单链表
'''
def reverse(head:ListNode)->ListNode:
    cur=head
    last=None
    while(cur):
        next=cur.next
        cur.next=last
        last=cur
        cur=next
    return last

'''
找倒数第k个结点
双指针，快的先走k步,直到走到null，此时慢指针即是倒数第k个
'''
def findNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    p1=head
    p2=head
    for i in range(0,n):
        p1=p1.next
    while p1:
        p1=p1.next
        p2=p2.next
    return p2

def hasCycle(head: Optional[ListNode]) -> bool:
    fast=head
    slow=head
    while(fast and fast.next):
        fast=fast.next.next
        slow=slow.next
        if(fast==slow):
            return True
    return False

l2=reverse(ListNode(12,ListNode(13,ListNode(14))))
l2.print()