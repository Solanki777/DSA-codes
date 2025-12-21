# here duplicates are exits
# you have to return true or false if exits or not
def search(nums,target):
    l=0
    h=len(nums)-1
    while l<=h:
        m=(l+h)//2

        # edge case
        if nums[m]==target:
            return True
        
        # remove duplicates nums=[7,7,7,1,3,7,7,7]
        while nums[l]==nums[m]==nums[h]:
            l+=1
            h-=1
            continue

        # left part is sorted?
        if nums[m]>=nums[l]:
            if nums[l]<=target<nums[m]:
                h=m-1
            else:
                l=m+1

        # right part sorted ?
        else:
            if nums[m]<target<=nums[h]:
                l=m+1
            else:
                h=m-1
    return False


nums=[10,11,11,12,12,13,13,13,1,2,3,4]
target=111
ans=search(nums,target)
print(ans)