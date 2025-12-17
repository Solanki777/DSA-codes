# lower bound[Smallest index such that nums[i]>=target] here we gona aaply method as we apply method in binary method

# here we given a sorted array then we have to divide arry as per mid Value

# if mid is still >=target then go in deep 

def lower_bound(nums,target):
    lb=len(nums)
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb



nums=[1,1,1,1,2,2,2,3,3,5,5,6,6,7,7,7,8,8,9,10,10,11,12,13]
target=7
ans=lower_bound(nums,target)
print(ans)

# upperbound:smallest index such that nums[i]<target

def upper_bound(nums,target):
    up=len(nums)
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            up=mid
            high=mid-1
        else:
            low=mid+1
    return up



nums=[1,1,1,1,2,2,2,3,3,5,5,6,6,7,7,7,8,8,9,10,10,11,12,13]
target=0
ans=upper_bound(nums,target)
print(ans)