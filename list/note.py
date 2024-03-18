from solution import ListNode

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

l2=reverse(ListNode(12,ListNode(13,ListNode(14))))
l2.print()