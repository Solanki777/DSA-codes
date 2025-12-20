def ocuu(nums,target):
    high=len(nums)-1
    low=0
    count=0
    lb=-1
    up=-1
    while low<=high:
        mid=(low+high)//2
        if target<=nums[mid]:
            high=mid-1
            if nums[mid]==target:

                        lb=mid
        else:
            low=mid+1
    
    if lb==-1:
        return 0
    
    low=0
    high=len(nums)-1
    up=len(nums)
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            high=mid-1
            up=mid
        else:
            low=mid+1

    up=up
    count=up-lb
    return count
            

nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
target=5
ans=ocuu(nums,target)
print("ans ",ans)

# time complexity is O(log n) and space compelxity is O(1)