# coding=utf-8

from typing import List
from typing import Optional

class Solution:
    '''
    最长回文子序列的解法：
    最长回文子串拆解为子问题的方式，s[l,r]表示字符串s中[l,r]部分的最长回文子串，初始l=0,r=n-1.
    if(s[l]==s[r]) 
        s[l,r]=s[l+1,r-1]+2
    else
        s[l,r]=max(s[l+1,r],s[l,r-1])
    '''
    def longestPalindrome(self, s: str) -> str:
        pass

    '''
    5. Longest Palindromic Substring
    因为子串要求连续，s[l,r]成立则必须s[l]=s[r]且s[l+1,r-1]也为回文子串
    dp[i][j]表示s[i...j]为回文串
    
    '''
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False for j in range(n)] for i in range(n)]
        res=[0,0]
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                res=[i,i+1]
        for span in range(2,n):
            for i in range(n-span):
                if s[i]==s[i+span] and dp[i+1][i+span-1]:
                    dp[i][i+span]=True
                    res=[i,i+span]
        l,r=res
        return s[l:r+1]

    def lengthOfLIS(self,nums:List[int])->int:
        n=len(nums)
        if n==0:
            return 0
        #init
        memo=[0]*n
        memo[n-1]=1
        #dp
        for i in range(n-2,-1,-1):
            after=0
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    after=max(after,memo[j])
            memo[i]=after+1
        return max(memo)

sol=Solution()
print(sol.longestPalindrome('jfskjjksfj'))