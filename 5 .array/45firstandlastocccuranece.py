# brute force solution:
# def first_last_occurance(nums,target):
#     f=-1
#     l=-1
#     for i in range(0,len(nums)):
#         if target==nums[i]:
#             f=i
#             l=i
#             i=i+1
#             while(i<=len(nums)-1 and nums[i]==target):
#                 l=i
#                 i+=1

#             break
    
#     return (f,l)


# time complexity is O(n) and space compelxity is O(1)


# nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
# target=1
# ans=first_last_occurance(nums,target)
# print(ans)

# optimal solution:if i get he lower bound and upper bound then i can return (l,u-1) lets try it
def first_last_occurance(nums,target):
    n=len(nums)
    def lower():
        low=0
        high=len(nums)-1
        l=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                high=mid-1
                l=mid
            else:
                low=mid+1
        if n>l and nums[l]==target:
            return l
        else:
            return -1
        
    def upper():
        low=0
        high=len(nums)-1
        u=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                u=mid
                high=mid-1
            else:
                low=mid+1
        return u
    
    first=lower()
    last=upper()-1
    if first==-1:
        return [-1,-1]
    else:
        return [first,last]



nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
target=10
ans=first_last_occurance(nums,target)
print(ans)