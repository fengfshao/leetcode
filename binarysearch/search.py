from typing import List

'''
标准的二分查找,注意l<=r
'''
def binsearch(nums,l,r,target):
    while l<=r:
        m=(l+r)//2
        if target==nums[m]:
            return m
        elif target<nums[m]:
            r=m-1
        else:
            l=m+1
    return -1

'''
二分查找,如果找不到,返回最接近小的如果less为true,否则返回最接近的大的
如果返回-1,则说明没有比target还小的
如果返回n,n=len(nums),则说明没有比target还大的
'''
def binsearch(nums,l,r,target,less):
    while l<=r:
        m=(l+r)//2
        if target==nums[m]:
            return m
        elif target<nums[m]:
            r=m-1
        else:
            l=m+1
    return r if less else l

'''
搜索最接近的
'''
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

'''
找第一个>=target的数
'''
def binsearchGreater(nums,l,r,target):
    while l<=r:
        m=(l+r)//2
        if target>nums[m]:
            l=m+1
        else:
            r=m-1
    return l


print(binsearchGreater([1,3,11,11],0,3,10))
