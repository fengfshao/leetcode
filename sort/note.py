from typing import List


'''
选择排序实现
T=O(n^2),S=O(1),不稳定排序
'''
def selectSort(nums):
    for i in range(len(nums)):
        minIdx=i; # 从[i...n]中选择选择最小的数放到i上，初始最小值为nums[i]
        for j in range(i+1,len(nums)):
            if(nums[j]<nums[minIdx]):
                minIdx=j
        nums[i],nums[minIdx]=nums[minIdx],nums[i]

'''
插入排序实现
T=O(n^2),S=O(1),稳定排序
近乎有序数组，效率极高，可提前终止循环
'''
def insertSort(nums):
    n=len(nums)
    for i in range(1,n):
        cur=nums[i]
        k=i-1 #[0,i-1]有序
        for j in range(i-1,0-1,-1):
            if(cur<nums[j]):
                nums[j+1]=nums[j]
                k=j
            else:
                break
        nums[k]=cur

'''
冒泡排序实现
T=O(n^2),效率比选择高，不如插入，S=O(1)稳定排序
记录某一趟是否产生了交换以提前结束
'''
def bubbleSort(nums):
    n=len(nums)
    swaped=1
    for j in range(n-1,1-1,-1): # j=n-1,j>=0,j--
        if(swaped==1):
            # 将[0,j-1]中最大的元素冒泡交换到j的位置
            swaped=0
            for i in range(0,j):
                if(nums[i]>nums[i+1]):
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    swaped=1
        else:
            break


'''
归并排序实现，T=O(n*logn)，S=O(n)，稳定排序
适合链表等多路排序
'''

def mergeSort(nums:List[int]):
    mergeSort0(nums,0,len(nums)-1)

def mergeSort0(nums,l:int,r:int):
    if(l>=r):
        return
    q=(l+r)//2
    print(l,r,q)
    mergeSort0(nums,l,q)
    mergeSort0(nums,q+1,r)
    left=nums[l:q+1]
    right=nums[q+1:r+1]
    idx1,idx2=0,0
    for i in range(l,r+1):
        if(idx1<len(left) and idx2<len(right)):
            if(left[idx1]<right[idx2]):
                nums[i]=left[idx1]
                idx1+=1
            else:
                nums[i]=right[idx2]
                idx2+=1
        elif(idx1<len(left)):
            nums[i]=left[idx1]
            idx1+=1
        else:
            nums[i]=right[idx2]
            idx2+=1

'''
堆排序实现,使用基于数组存储的完全二叉树
T=O(n*logn), S=O(1),不稳定排序
'''
def heapsort(nums):
    pass

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
            j-=1
            nums[j],nums[i+1]=nums[i+1],nums[j]
    nums[l]=nums[i]
    nums[i]=base
    return i

nums=[3,7,2,5,1,4,0,12,9,4]            
mergeSort(nums)
print(nums)