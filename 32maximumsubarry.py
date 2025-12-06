# you have to create the subarry having the maximum sum and return that sum only . first we use only the brute force solution where form starting we gona doing summation increation arry and find the maximum

# brute force soltuion:
# def sub_sum(nums):
#     maxi=float("-inf")
#     for i in range(0,len(nums)):
#         total=0
#         for j in range(i,len(nums)):
#             total=total+nums[j]
#             maxi=max(maxi,total)
#     return maxi            


# nums=[-2,1,-3,4,-1,2,1,-5,4]
# ans=sub_sum(nums)
# print(ans)

# time complexity is O(n^2) and space compexity is O(1)

# optimal solution: here we gona use the kadane's algorithm 
# in kadan's algorithm: whatch apna college video for better  

def kadan(nums):
    sum=0
    max_sum=0
    for el in nums:
        sum+=el
        max_sum=max(sum,max_sum)
        if sum<0:
            sum=0
    return max_sum

nums=[-2,1,-3,4,-1,2,1,-5,4]
ans=kadan(nums)
print(ans)

# time complexity is O(n)