from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        cur,res=self,str(self.val)
        while(cur.next):
            res+="->"+str(cur.next.val)
            cur=cur.next
        return res

class Solution:
    '''
    1. Two Sum
    直观解法需要两层遍历来确定是否存在两个数字，sum为target值
    但是由于这两个值有固定关系，即num2=target-num1，因此当遇到
    num1时，可以直接得出需要的num2，因此可以借助查找解决问题。
    类似最简单的题目，给定一组数，使用O(1)复杂度判断某个数是否存在。
    '''
    def twoSum0(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            dict[nums[i]]=i
        for i in range(0,len(nums)):
            num2=target-nums[i]
            idx2=dict[num2]
            if idx2 and idx2!=i :
                return [i,dict[num2]]
        return []

    '''
    1. Two Sum
    实际上无需先将所有数放到map里再去查找，可以边放边查找，
    因为遍历到num1时，即使num2不在map中，
    但是当遍历到num2时，num1已经存在map中。
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            num2=target-nums[i]
            if num2 in dict:
                return [i,dict[num2]]
            dict[nums[i]]=i
        return []
    '''
    
    2. Add Two Numbers
    两个数求和，遍历链表，两个数的加法实际上也是从个位到高位的，
    因此题目的`digits are stored in reverse order`正好。
    ps: 需要注意进位后产生新的最高位，如两个3位数相加产生4位数
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1,cur2=l1,l2
        res=cur3=ListNode(-1)
        extra=0
        while cur1 or cur2:
            if cur1:
                extra+=cur1.val
                cur1=cur1.next
            if cur2:
                extra+=cur2.val
                cur2=cur2.next
            cur3.next=ListNode(extra%10)
            cur3=cur3.next
            extra=extra//10
        if extra>0:
            cur3.next=ListNode(extra)
        return res.next

    '''
    3. Longest Substring Without Repeating Characters
    经典滑动窗口解法，使用set去重
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,n,res=0,-1,len(s),0
        chars=set()
        while(r+1<n):
            if(s[r+1] not in chars):
                chars.add(s[r+1])
                r+=1
            else:
                chars.remove(s[l])
                l=l+1
            res=max(res,r-l+1)
        return res
        
    '''
    26. Remove Duplicates from Sorted Array
    删除有序数组中的重复元素，双指针思路一遍扫描，[0...i]存放不重复的递增元素，j遍历数组
    '''        
    def removeDuplicates(self, nums: List[int]) -> int:
        assert len(nums)>0
        i=0
        for j in range(1,len(nums)):
            if(nums[j]!=nums[i]):
                i+=1
                nums[i]=nums[j]
        return i+1

sol=Solution()
# print(sol.twoSum([1,2,3,4],6))
nums=[1,2,2,6]
print(sol.removeDuplicates(nums))
print(nums)
# l1=ListNode(3,ListNode(2,ListNode(1)))
# l2=ListNode(7,ListNode(8,ListNode(9)))
# print(l1)
# print(sol.addTwoNumbers(l1,l2))
#print(sol.lengthOfLongestSubstring("abcbef"))

