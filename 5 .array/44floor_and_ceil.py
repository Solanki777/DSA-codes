# here i have to find the floor and ceil value of the gien target
def f_and_c(nums,target):
    right=len(nums)-1
    left=0
    f=-1
    c=-1

    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return [nums[mid],nums[mid]]
        elif nums[mid]<target:
            f=nums[mid]
            left=mid+1
        else:
            c=nums[mid]
            right=mid-1

    return (f,c)

# time compelxity is O(logn) and space complexity is O(1)

target=2
nums=[3,4,4,4,8,9,9,10,12,12,14,15]
ans=f_and_c(nums,target)
print(ans)

