def minimum(nums):
    low=0
    high=len(nums)-1
    ans=float("inf")
    while low<=high:
        mid=(low+high)//2
        
        # sorted part if right
        if nums[mid]<nums[high]:
            ans=min(ans,nums[mid])
            high=mid-1
        
        # sorted part if right
        else:
            ans=min(ans,nums[mid])
            low=mid+1
    return ans



nums=[4,5,6,7,0,1,2]
print(minimum(nums))

# here we have to return minimum from the array

# time compelexity is O(logn) and space complexity is O(1)