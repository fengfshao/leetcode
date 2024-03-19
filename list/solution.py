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
     
     '''
     2. Add Two Numbers
     最低位在链表头，正好直接遍历
     '''
     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
          cursum=0
          head=ListNode(-1)
          cur=head
          while(l1 or l2):
               if(l1):
                    cursum+=l1.val
                    l1=l1.next
               if(l2):
                    cursum+=l2.val
                    l2=l2.next
               cur.next=ListNode(cursum%10)
               cur=cur.next
               cursum=cursum//10
          if(cursum>0):
               cur.next=ListNode(cursum)
          return head.next
     
     '''
     19. Remove Nth Node From End of List
     使用双指针的思路找倒数n+1个点，使用额外头结点统一对边界情况的处理
     '''
     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
          newHead=ListNode(-1)
          newHead.next=head
          prev=self.findNthFromEnd(newHead,n+1)
          prev.next=prev.next.next
          return newHead.next

     def findNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
          p1=head
          p2=head
          for i in range(0,n):
               p1=p1.next
          while p1:
               p1=p1.next
               p2=p2.next
          return p2
     
     '''
     21. Merge Two Sorted Lists
     '''
     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
          dh=ListNode(-1)
          cur=dh
          while(list1 or list2):
               if(list1 and list2):
                    if(list1.val<=list2.val):
                         cur.next=list1.val
                         list1=list1.next
                    else:
                         cur.next=list2.val
                         list2=list2.next
               elif(list1):
                    cur.next=list1
               else:
                    cur.next=list2
               cur=cur.next
          return dh.next

     '''
     24. Swap Nodes in Pairs
     '''
     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
          if(head and head.next):
               left=self.swapPairs(head.next.next)
               next=head.next
               head.next=left
               next.next=head
               return next
          else:
               return head
     '''
     61. Rotate List
     类似19题
     '''
     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
          newHead=ListNode(-1)
          newHead.next=head
          prev=self.findNthFromEnd(newHead,k+1)
          border=prev.next
          tmp=border
          while(tmp.next):
               tmp=tmp.next
          tmp.next=newHead.next
          prev.next=None
          return border
          
sol=Solution()
