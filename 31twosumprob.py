# nums=[5,9,1,2,4,15,6,3]
# here you have to return the index where the sum of value at those index is equal to the target . here you can not take one value twice.
# def twopro(nums,target):
#     i=0
#     j=0
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)-1):
#             if i==j:
#                 continue
#             if nums[i]+nums[j]==target:
#                 return [i,j]


# nums=[5,9,1,2,4,15,6,3]
# ans=twopro(nums,13)
# print(ans)

# timecomplexity is O(n^2) ans space compelxity is O(1)

# optimal soution we use dictonary method
def twopro(nums,target):
    dicto={}
    for el in range(0,len(nums)-1):
        remaining=target-nums[el]
        if remaining in dicto:
            return [dicto[remaining],el]
        else:
            dicto[nums[el]]=el



nums=[5,9,1,2,4,15,6,3]
ans=twopro(nums,13)
print(ans)


# here the time complexity is O(N) and space complexity is O(N)