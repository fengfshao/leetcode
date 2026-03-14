# coding=utf-8

from typing import List
from typing import Optional

class Solution:

    '''
    这个问题具备贪心的性质,只要明天的价格比今天高，我们就今天买入并在明天卖出。
    因为可以看到未来的价格,因此卖出后根据情况再买回,这样即使股价连续上涨（例如从 $1 涨到 $3，再涨到 $5），
    也可以将其拆分为多次交易.
    122. Best Time to Buy and Sell Stock II
    '''
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                res+=prices[i]-prices[i-1]
        return res

    '''
    55. Jump Game
    直观naive的版本,会超时
    '''
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[False]*n
        dp[0]=True
        for i in range(1,n):
            for j in range(0,i) :
                dp[i]=dp[j] and nums[j]>=i-j
                if dp[i]:
                    break
        return dp[n-1]

    '''
    贪心解法,贪心不在于在每个位置跳几步,而是记录一个最远能到的位置
    '''
    def canJump2(self, nums: List[int]) -> bool:
        farthest=0
        n=len(nums)
        for i in range(0,n):
            if i>farthest:
                return False
            farthest=max(farthest,i+nums[i]) 
            if farthest>=n-1:
                return True 
        return False

sol=Solution()
nums=[2,5,0,0]
print(sol.canJump2(nums))
print(nums)
        

        