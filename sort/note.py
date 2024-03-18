from typing import List

'''
快速排序实现
'''
def quicksort(nums): 
    quicksort0(nums,0,len(nums)-1)    
    
def quicksort0(nums:List[int],l:int,r:int):
    if(l<r):
        q=partition(nums,l,r)
        quicksort0(nums,l,q-1)
        quicksort0(nums,q+1,r)

def partition(nums:List[int],l:int,r:int)->int:
    # nums[l+1,i]<=base , nums[j,r]>base
    base=nums[l]
    i=l
    j=r+1
    while(i<j-1):
        if(nums[i+1]<=base):
            i+=1
        else:
            tmp=nums[j-1]
            nums[j-1]=nums[i+1]
            nums[i+1]=tmp
            j-=1
    nums[l]=nums[i]
    nums[i]=base
    return i

nums=[3,7,2,5,1,4,0,12,9,4]            
quicksort(nums)
print(nums)
        
        