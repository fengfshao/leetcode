class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers0(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[int]:
        prev=0
        if(l1.next and l2.next):
             prev=addTwoNumbers0(l1.next,l2.next);
        elif(l1.next and not l2.next):
             prev=addTwoNumbers0(l1.next,l2);
        elif(l2.next and not l1.next):
             prev=addTwoNumbers0(l1,l2.next);
        cur=0
        if(l1 and l2):
             cur=l1.val+l2.val
        elif(l1):
             cur=l1.val
        elif(l2):
             cur=l2.val
        return cur