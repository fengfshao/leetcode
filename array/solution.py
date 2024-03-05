# coding=utf-8

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
    使用map记录扫描过的数字，避免二重循环
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
    4. Median of Two Sorted Arrays
    TODO
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass
    
    '''
    11. Container With Most Water
    双指针方法，i,j初始放置两端，由于长度缩短，潜在更大的容量需要更高的两壁，高度取决于两边较低的一个
    因此当左边相对较低时潜在值只可能在[i+1,j]，右边较低时潜在值只能在[i,j-1]
    '''
    def maxArea(self, height: List[int]) -> int:
        assert len(height)>=2
        i,j=0,len(height)-1
        res=0
        while(i<j):
            res=max(res,min(height[i],height[j])*(j-i))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return res

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
    6. Zigzag Conversion
    之字形打印，一种直观的解法，将每个字符放到对应的行中，最后拼接结果
    一次循环包括之形打印，如A->B->C->D
    A   E
    B D F
    C 
    '''
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        rows=[[] for i in range(numRows)]
        idx=0
        while(idx<len(s)):
            for i in range(0,numRows):
                if idx<len(s):
                    rows[i]+=s[idx]
                    idx+=1
            for i in range(1,numRows-1):
                if idx<len(s):
                    rows[numRows-1-i]+=s[idx]
                    idx+=1
        for i in range(0,len(rows)):
            rows[i]=''.join(rows[i])
        return ''.join(rows)
        
    '''
    7. Reverse Integer
    逐位解析再计算，类似parseInt。
    '''
    def reverse(self, x: int) -> int:
        pass

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

# print(sol.removeDuplicates(nums))
# print(nums)

# print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
# print(sol.maxArea([3,3]))
# l2=ListNode(7,ListNode(8,ListNode(9)))
# print(l1)
# print(sol.addTwoNumbers(l1,l2))
#print(sol.lengthOfLongestSubstring("abcbef"))

MAX_INT=2^31-1
MIN_INT=-2^31
a=24345
while a>0:
    print(a%10)
    a//=10

sol=Solution()    
print(sol.convert('PAYPALISHIRING',1))
