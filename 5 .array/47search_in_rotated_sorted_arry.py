
# bruteforxe:time complexity O(n)
def search(nums,target):
    for el in range(len(nums)):
        if nums[el]==target:
            return el
        
    return -1
nums=[1,4,5,6,8,9,10,11,15,20]
ans=search(nums,6)
print(ans)

# originally array is sorted in ascending order nums=[0,1,2,3,4,5,6,7,8,9] now array is roated n times here n is unkonwn and also the values are distinct

# nums=[3,4,5,6,7,8,9,0,1,2]
# after getting the mid value we can see either left or right part is always sorted in above example the mid is 5 index which is 8 so left part is sorted so we can apply the binary search their

# step 1:find the sorted part left or right
# step 2: then aaply the binary search conditions if it is aaplicable to find the target

def search(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if target==nums[mid]:
            return mid
        
        # left sorted part?
        if nums[low]<nums[mid]:
            if nums[low]<=target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
            
        # right sorted part?
        else:
            if nums[mid]<target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return -1



nums=[1,4,5,6,8,9,10,11,15,20]
ans=search(nums,6)
print(ans)


        

# time compelxity is O(log n) and space compelxity is O(1)