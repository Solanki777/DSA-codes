# 1.arry is sorted
# 2.return the position where the target to be inserted

# search insert position
def insert_pos(nums,target):
    low=0
    high=len(nums)-1
    lb=len(nums)
    while(low<=high):
        mid=(low+high)//2

        if nums[mid]>=target:
            lb=mid
            high=mid-1
            
        else:
            low=mid+1
        
    return lb
            

# time complexity is O(logbase2N) and space complexity is O(1)

nums=[1,3,4,5,8,9,14,15,19,20,21]
target=19
ans=insert_pos(nums,target)
print(ans)