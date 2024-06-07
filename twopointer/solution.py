from typing import Optional
from typing import List
import queue
from collections import deque
import heapq
import random

class Solution:

    '''
    5. Longest Palindromic Substring
    动态规划
    memo[i][j]取决于 s[i]==s[j] and memo[i+1][j-1] 
    初始状态: memo[i]都为true,memo[i][i+1]
    '''
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        res = [0, 0]
        for i in range(n):
            memo[i][i]=True
            if i+1<n and s[i]==s[i+1]:
                memo[i][i+1]=True
                res=[i,i+1]
        for span in range(2,n):
            for i in range(0,n-span):
                j=i+span
                if s[i]==s[j] and memo[i+1][j-1]:
                    memo[i][j]=True
                    res=[i,j]
        i,j=res
        return s[i:j+1]

    
    '''
    11. Container With Most Water
    双指针遍历，本质是剪枝，如果更长的边界往中间移动，不会得到比当前更大的值，因此每次移动短的边界
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
    15. 3Sum
    排序后，在nums[i]的右侧的区间找两个数，使其和为-nums[i],类似二分
    https://www.jianshu.com/p/232a54fd1333
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            l,r=i+1,n-1
            twosum=nums[l]+nums[r]
            while(l<r):
                if(twosum+nums[i]>0):
                    r-=1
                elif(twosum+nums[i]<0):
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l+=1
                    r-=1
        return res
    

    '''
    16. 3Sum Closest
    思路类似3Sum，只是判断差值绝对值的最小值即可，此时的三个数即为解
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        pass


    '''
    18. 4Sum
    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pass

    '''
    75. Sort Colors
    使用双指针可以将数组分为三部分[0,i],[i+1,j-1],[j,n)
    https://zhuanlan.zhihu.com/p/113385463
    '''
    def sortColors(self, nums: List[int]) -> None:
        i,j=-1,len(nums)
        cur=0
        while cur<j: 
            if nums[cur]==0:
                i+=1
                nums[i],nums[cur]=nums[cur],nums[i]
                cur+=1
            elif nums[cur]==2:
                j-=1
                nums[j],nums[cur]=nums[cur],nums[j]
            else:
                cur+=1

    
sol=Solution()
colors=[2,0,1]
sol.sortColors(colors)
print(colors)
