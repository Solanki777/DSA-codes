# arr=[1,0,1,0,1,1,1,0,1,1,1,1,0,1]
# here in this problem we try to return the maximum occurunce of 1 in the arry and the return that occurace like here 1 repeates 4 times maximum so return 4
def max_consucative(nums):
    max_co=0
    count=0
    for el in  nums:
        if el==1:
            count+=1
            max_co=max(max_co,count)
        if el==0:
            count=0

    return max_co

nums=[1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1]
ans=max_consucative(nums)
print(ans)


# timecoplexity is O(n) and space complexity is O(1)