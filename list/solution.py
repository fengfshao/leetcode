from typing import Optional
import queue

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

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

     def print(self):
          q=queue.Queue()
          q.put(self)
          while(not q.empty()):
               node=q.get()
               print(str(node.val),end=' ')
               if(node.left):
                    q.put(node.left)
               if(node.right):
                    q.put(node.right)
          print('')



def mkList(nums):
     dummyHead=ListNode(-1)
     cur=dummyHead
     for num in nums:
          cur.next=ListNode(num)
          cur=cur.next
     return dummyHead.next

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
     递归地求解问题
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
          n=0
          cur=head
          last=None
          while(cur):
               n+=1
               last=cur
               cur=cur.next 
          if(n<=1):
               return head
          k=k%n # 旋转n次回原形
          if(k==0):
               return head
          prev=self.findNthFromEnd(head,k+1)
          right=prev.next
          prev.next=None
          last.next=head
          return right

     '''
     82. Remove Duplicates from Sorted List II
     没啥特别的技巧，主要是以窗口为单位判断是否需要输出，遍历后注意尾部处理
     '''
     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
          dummyHead=ListNode(-1)
          last=dummyHead
          if(not head or not head.next):
               return head
          lastn=1
          lastval=head.val
          lastNode=head
          cur=head.next
          while(cur):
               if(lastval!=cur.val):
                    if(lastn==1):
                         last.next=lastNode
                         last=last.next
                    lastn=1
                    lastval=cur.val
                    lastNode=cur
               else:
                    lastn+=1
               cur=cur.next
          if(lastn==1):
               last.next=lastNode
          else:
               last.next=None
          return dummyHead.next

     '''
     83. Remove Duplicates from Sorted List
     只需把next和当前对比即可，遇到一样的就往下走
     ''' 
     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
          cur=head
          while(cur and cur.next):
               if(cur.val==cur.next.val):
                    cur.next=cur.next.next
               else:
                    cur=cur.next
          return head
     
     '''
     86. Partition List
     链表分为两部分,一遍扫描
     '''
     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
          left=ListNode(-1)
          right=ListNode(-1)
          curleft=left
          curright=right
          cur=head
          while(cur):
               if(cur.val<x):
                    curleft.next=cur
                    curleft=curleft.next
               else:
                    curright.next=cur
                    curright=curright.next
               cur=cur.next
          curleft.next=right.next
          curright.next=None
          return left.next
     '''
     92. Reverse Linked List II
     注意反转完控制上左边和右边的处理
     ''' 
     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
          assert head
          n=right-left+1
          prevStart=None
          start=head
          for i in range(1,left):
               prevStart=start
               start=start.next
          cur=start
          last=None
          prevCur=None
          for i in range(0,n):
               next=cur.next
               cur.next=last
               last=cur
               prevCur=cur
               cur=next
          if(cur):
               start.next=cur
          if(prevStart):
               prevStart.next=prevCur
               return head
          else:
               return prevCur

     '''
     109. Convert Sorted List to Binary Search Tree
     思路类似根据中序+前/后序恢复二叉树，不同的是这里从有序链表的中间结点开始划分
     ''' 
     def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
          '''
          寻找链表的中间位置，左开右闭
          '''
          def middle(start,end):
               slow=start
               fast=start
               while(fast!=end and fast.next!=end):
                    fast=fast.next.next
                    slow=slow.next
               return slow
          
          def mkTree(start,end):
               if(start==end):
                    return None
               root=middle(start,end)
               left=mkTree(start,root)
               right=mkTree(root.next,end)
               rootNode=TreeNode(root.val,left,right)
               return rootNode

          return mkTree(head,None)

sol=Solution()
sol.sortedListToBST(mkList([-10,-3,0,5,9])).print()