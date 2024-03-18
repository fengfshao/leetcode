from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

     def print(self):
          cur=self
          while(cur):
               if(cur.next):
                    print(str(cur.val), end='->')
               else:
                    print(cur.val)
               cur=cur.next

class Solution: 
     def addTwoNumbers0(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[int]:
          prev=0
          if(l1.next and l2.next):
               prev=self.addTwoNumbers0(l1.next,l2.next)
          elif(l1.next and not l2.next):
               prev=self.addTwoNumbers0(l1.next,l2)
          elif(l2.next and not l1.next):
               prev=self.addTwoNumbers0(l1,l2.next)
          cur=0
          if(l1 and l2):
               cur=l1.val+l2.val
          elif(l1):
               cur=l1.val
          elif(l2):
               cur=l2.val
          return cur

     def reverse(self,head:ListNode)->ListNode:
          cur=head
          last=None
          while(cur):
               tmp=cur.next
               cur.next=last
               last=cur
               cur=tmp
          return last
     
     def reverse(self,head:ListNode,from:int,to)

sol=Solution()
l2=sol.reverse(ListNode(12,ListNode(13,ListNode(14))))
l2.print()