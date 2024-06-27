from typing import Optional
from typing import List
import queue
from collections import deque
import heapq
import random
import math

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


    '''
    88. Merge Sorted Array
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums3=nums1[0:m]
        i,j,k=0,0,0
        while i<m or j<n:
            if i<m and j<n:
                if nums3[i]<nums2[j]:
                    nums1[k]=nums3[i]
                    k+=1
                    i+=1
                else:
                    nums1[k]=nums2[j]
                    k+=1
                    j+=1
            elif i<m:
                nums1[k]=nums3[i]
                k+=1
                i+=1
            else:
                nums1[k]=nums2[j]
                k+=1
                j+=1

    '''
    125. Valid Palindrome
    '''
    def isPalindrome(self, s: str) -> bool:
        newstr=''.join(filter(str.isalnum, s)).lower()
        i,j=0,len(newstr)-1
        while i<j:
            if newstr[i]!=newstr[j]:
                return False
            i+=1
            j-=1
        return True
                
    '''
    151. Reverse Words in a String
    这个题可以通过两次翻转的办法,先将词倒过来,后面再去除多余的空格
    python字符串不可变
    '''
    def reverseWords(self, s: str) -> str:
        pass

    '''
    165. Compare Version Numbers
    循环比较数字部分
    '''
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1=list(map(int, version1.split('.')))
        nums2=list(map(int, version2.split('.')))
        n=max(len(nums1),len(nums2))
        for i in range(n):
            v1,v2=0,0
            if i <len(nums1): v1=nums1[i]
            if i <len(nums2): v2=nums2[i]
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
        return 0 

    '''
    167. Two Sum II - Input Array Is Sorted
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        while(l<r):
            sum=numbers[l]+numbers[r]
            if sum<target:
                l+=1
            elif sum>target:
                r-=1
            else:
                return [l+1,r+1]
        return [0,0]

    '''
    189. Rotate Array
    基于两次翻转的思路,实现局部有序,整体倒序
    '''
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseBetween(nums,l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        reverseBetween(nums,0,len(nums)-1)
        reverseBetween(nums,0,k-1)
        reverseBetween(nums,k,len(nums)-1)

    '''
    283. Move Zeroe
    维护好索引即可
    '''
    def moveZeroes(self, nums: List[int]) -> None:
        last=-1
        for i in range(len(nums)):
            if nums[i]!=0:
                last+=1
                nums[last]=nums[i]
        for i in range(last+1,len(nums)):
            nums[i]=0

    '''
    344. Reverse String
    '''
    def reverseString(self, s: List[str]) -> None:
        l,r=0,len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1

    '''
    345. Reverse Vowels of a String
    '''
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        l,r=0,n-1
        vowels=['a','e','i','o','u','A','E','I','O','U']
        chs=list(s)
        while l<r:
            while l<r and chs[l] not in vowels:
                l+=1
            while r>l and chs[r] not in vowels:
                r-=1
            if l<n and r>=0:
                chs[l],chs[r]=chs[r],chs[l]
                l+=1
                r-=1
        return ''.join(chs)

    '''
    349. Intersection of Two Arrays
    ''' 
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1=len(nums1)
        n2=len(nums2)
        p1,p2=0,0
        res=set()
        while p1<n1 and p2<n2:
            if nums1[p1] == nums2[p2]:
                res.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return list(res)

    '''
    350. Intersection of Two Arrays II
    '''
    def intersectII(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1=len(nums1)
        n2=len(nums2)
        p1,p2=0,0
        res=[]
        while p1<n1 and p2<n2:
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return list(res)
    
    '''
    392. Is Subsequence
    '''
    def isSubsequence(self, s: str, t: str) -> bool:
        ps,pt=0,0
        while ps<len(s) and pt<len(t):
            if s[ps]==t[pt]:
                ps+=1
                pt+=1
            else:
                pt+=1
        return not ps<len(s)

    '''
    443. String Compression
    基于滑动窗口的思路
    '''
    def compress(self, chars: List[str]) -> int:
        l,r,win=0,0,1
        res=[]
        n=len(chars)
        while l<n:
            while r+1<n and chars[r+1]==chars[l]:
                r+=1
                win+=1
            res.append(chars[l])
            if win>1:
                res.extend(str(win))
                win=1
            l=r=r+1
        for i in range(len(res)):
            chars[i]=res[i]
        return len(res) 
    
    '''
    457. Circular Array Loop
    题目没太看懂
    '''
    def circularArrayLoop(self, nums: List[int]) -> bool:
        pass

    '''
    475. Heater
    主要是基于二分查找寻找离得最近的heater
    '''
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def binsearchMost(nums,target):
            l,r=0,len(nums)-1
            while l<=r:
                m=(l+r)//2
                if target==nums[m]:
                    return m
                elif target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            if r==-1:
                return l
            elif l==len(nums): 
                return r
            else:
                d1,d2=abs(nums[l]-target),abs(nums[r]-target)
                return l if d1<d2 else r

        heaters.sort()
        res=0
        for i in range(len(houses)):
           idx=binsearchMost(heaters,houses[i])
           dist=abs(heaters[idx]-houses[i])
           res=max(res,dist)
        return res

    '''
    481. Magical String
    '''    
    def magicalString(self, n: int) -> int:
        pass

    '''
    522. Longest Uncommon Subsequence II
    '''
    def findLUSlength(self, strs: List[str]) -> int:
        pass


    '''
    524. Longest Word in Dictionary through Deleting
    循环判断字典的每个字符串是不是输入的子串
    '''
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubsequence(s,x):
            i,j=0,0
            for i in range(len(s)):
                if s[i]==x[j]: j+=1
                if j>=len(x): return True
             
        res=""
        resList=[""]
        for x in dictionary:
            if len(x)>=len(res) and isSubsequence(s,x):
                if len(x)>len(res):
                    resList=[]
                res=x
                resList.append(res)
        resList.sort()
        return resList[0]


    '''
    532. K-diff Pairs in an Array
    '''
    def findPairs(self, nums: List[int], k: int) -> int:
        visited=set()
        res=set()
        for num in nums:
            if num+k in visited:
                res.add(num)
            if num-k in visited:
                res.add(num-k)
            visited.add(num)
        return len(res)

    '''
    541. Reverse String II
    '''
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(chs,l,r):
            while l<r:
                chs[l],chs[r]=chs[r],chs[l]
                l+=1
                r-=1
        i,n=0,len(s)
        chs=list(s)
        while i<n:
            j=min(i+k-1,n-1)
            print(i,j)
            reverse(chs,i,j)
            print(chs)
            i+=2*k
        return ''.join(chs)

    '''
    557. Reverse Words in a String III
    '''
    def reverseWordsIII(self, s: str) -> str:
        def reverse(chs,l,r):
            while l<r:
                chs[l],chs[r]=chs[r],chs[l]
                l+=1
                r-=1
        i,n=0,len(s)
        chs=list(s)
        while i<n:
            j=i
            while j<n and chs[j]!=' ':
                j+=1
            reverse(chs,i,j-1)
            i=j+1
        return ''.join(chs)

    '''
    611. Valid Triangle Number
    三角形判断条件a+b>c && a+c>b && b+c>a可简化为a+b>c,当a<=b<=c时
    因此可以将数组排序后进行搜索,避免O(n^3)的暴力搜索
    '''
    def triangleNumber(self, nums: List[int]) -> int:
        #找第一个>=target的数
        def search(nums,l,r,target):
            while l<=r:
                m=(l+r)//2
                if target>nums[m]:
                    l=m+1
                else:
                    r=m-1
            return l 

        nums.sort()
        n=len(nums)
        res=0
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                k=search(nums,j+1,n-1,nums[i]+nums[j])
                #从k开始(包含k)后面的数都是nums[k]>=nums[i]+nums[j]
                res+=k-1-j
        return res

    '''
    633. Sum of Square Numbers
    '''
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c)) + 1):
            b = math.sqrt(c - i*i)
            if b==int(b):
                return True
        return False

    '''
    647. Palindromic Substrings
    类似第五题,采用动态规划避免重复搜索
    '''
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        res=n
        for i in range(n):
            memo[i][i]=True
            if i+1<n and s[i]==s[i+1]:
                memo[i][i+1]=True
                res+=1
        for span in range(2,n):
            for i in range(0,n-span):
                j=i+span
                if s[i]==s[j] and memo[i+1][j-1]:
                    memo[i][j]=True
                    res+=1
        return res
     
    '''
    658. Find K Closest Elements
    使用滑动窗口寻找，可以使用二分进一步优化，如先二分搜索一个最近的i，最近的元素一定在窗口里，此时确定一个窗口[i-k+1,i+k-1]，再通过滑动缩小窗口
    '''
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r=0,len(arr)-1
        while r-l+1>k:
            if abs(arr[l]-x)>abs(arr[r]-x):
                l+=1
            else:
                r-=1
        return arr[l:r+1]

   
    '''
    821. Shortest Distance to a Character
    利用二分搜索寻找最近的字符
    '''
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def binsearchMost(nums,target):
            l,r=0,len(nums)-1
            while l<=r:
                m=(l+r)//2
                if target==nums[m]:
                    return m
                elif target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            if r==-1:
                return l
            elif l==len(nums): 
                return r
            else:
                d1,d2=abs(nums[l]-target),abs(nums[r]-target)
                return l if d1<d2 else r
        idxs,res=[],[]
        for i in range(0,len(s)):
            if s[i]==c: idxs.append(i)
        for i in range(0,len(s)):
            j=binsearchMost(idxs,i)
            res.append(abs(idxs[j]-i))
        return res

    '''
    832. Flipping an Image
    类似反转字符串，同时使用异或翻转比特 
    '''
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            l,r=0,len(row)-1
            while l<=r:
                row[l],row[r]=row[r]^1,row[l]^1
                r-=1
                l+=1
        return image


    '''
    905. Sort Array By Parity
    采用快排partition的思路
    '''
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        i,j=l-1,r+1
        while i<j-1:
            if nums[i+1]%2==0:
                i+=1
            else:
                j-=1
                nums[j],nums[i+1]=nums[i+1],nums[j]
        return nums
    

    '''
    917. Reverse Only Letters
    翻转字符串的变种，仅当特定字符采考虑翻转
    '''
    def reverseOnlyLetters(self,s: str) -> str:
        l,r=0,len(s)-1
        chs=list(s)
        while l<r:
            while l<r and not chs[l].isalpha():
                l+=1
            while r>l and not chs[r].isalpha():
                r-=1
            if l<len(s) and r>=0:
                chs[l],chs[r]=chs[r],chs[l]
                l+=1
                r-=1
        return ''.join(chs) 

    '''
    680. Valid Palindrome II
    回溯的思路判断需要删字符的情况
    '''
    def validPalindrome(self, s: str) -> bool:
        def judge(s,l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return judge(s,l+1,r) or judge(s,l,r-1)
            else:
                l+=1
                r-=1   
        return True

    '''
    696. Count Binary Substrings
    重点是借助group数组的思路
    '''
    def countBinarySubstrings(self, s: str) -> int:
        group=[1]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                group[-1]+=1
            else:
                group.append(1)
        res=0
        for i in range(0,len(group)-1):
            res+=min(group[i],group[i+1])
        return res

    '''
    763. Partition Labels
    重点在题目的贪心的思路
    '''
    def partitionLabels(self, s: str) -> List[int]:
        last=[0]*26
        for i in range(len(s)):
            last[ord(s[i])-97]=i
        l,r=0,0
        res=[]

        for i in range(len(s)):
            r = max(r, last[ord(s[i])-97])
            if (i == r):
                res.append(r - l + 1)
                l= i + 1
        return res

    '''
    795. Number of Subarrays with Bounded Maximum
    多个办法,可以采用dp或前缀和思路,见https://www.bilibili.com/read/cv20004884/
    '''
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def notGreaterThan(nums,target):
            cnt=0
            t=0
            for num in nums:
                t=0 if num>target else t+1
                cnt+=t
            return cnt
        return notGreaterThan(nums,right)-notGreaterThan(nums,left-1)

    '''
    809. Expressive Words
    统计每个分组的次数,对比每个分组是否长了超过3
    '''
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compress(s):
            res=[[s[0],1]]
            for i in range(1,len(s)):
                if s[i]==s[i-1]:
                    res[-1][1]+=1
                else:
                    res.append([s[i],1])
            return res

        res=0
        groups=compress(s)
        for word in words:
            g=compress(word)
            if len(g)==len(groups):
                stretchy=True
                for i in range(0,len(g)):
                    if groups[i][0]!=g[i][0]: 
                        stretchy=False
                        break
                    if groups[i][1]<g[i][1]:
                        stretchy=False
                        break 
                    if groups[i][1]>g[i][1] and groups[i][1]<3:
                        stretchy=False
                        break
                if stretchy: res+=1 
        return res

    '''
    826. Most Profit Assigning Work
    基于二分查找寻找最大可以干的工作,
    然后基于前缀和的思路预先算出截止到每个difficuty可以做的最大工作
    '''
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pairs=[]
        for i in range(0,len(difficulty)):
            pairs.append([difficulty[i],profit[i]])
        pairs.sort()
        maxprofit=[0]*len(profit)
        maxprofit[0]=pairs[0][1]
        for i in range(1,len(profit)):
            maxprofit[i]=max(maxprofit[i-1],pairs[i][1])
        res=0
        for w in worker:
            l,r=0,len(difficulty)-1
            while l<=r:
                m=(l+r)//2
                if pairs[m][0]<=w:
                    l=m+1
                else:
                    r=m-1
            if l!=0:
                res+=maxprofit[l-1]
        return res



sol=Solution()
# colors=[1,2,3,0,0,0]
# sol.merge(colors,3,[2,5,6],3)
# print(sol.isPalindrome("A man, a plan, a canal: Panama"))
# str1='abcd'
# print(sol.compareVersion("1.0.1","1"))
nums=[0,1,0,3,12]
#print(sol.compress(["a","a","b","b","c","c","c"]))
#print(sol.findLongestWord("abpcplea",dictionary = ["ale","apple","monkey","plea"]))
#print(sol.findClosestElements(arr = [1,1,1,10,10,10], k = 1, x = 9))
print(sol.maxProfitAssignment(difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]))
