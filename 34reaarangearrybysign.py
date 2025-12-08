# nums=[5,10,-3,-1-10,6] here we have to reaaarnge arry like +,-,+,- like sign 


# my solution:
# def rearr(nums):
#     for i in range(len(nums)):
#         if i%2==0:
#             if nums[i]<=0:
#                 for j in range(i+1,len(nums)):
#                     if nums[j]>=0:
#                         nums[i],nums[j]=nums[j],nums[i]
#                         break
#         else:
#             if nums[i]>0:
#                 for j in range(i+1,len(nums)):
#                     if nums[j]<0:
#                         nums[i],nums[j]=nums[j],nums[i]
#                         break
#     print(nums)

# nums=[5,10,-3,-1,-10,6]
# rearr(nums)

# this is solution has timecoplexity of O(N^2) and space compelxity is O(1) also this give diffrent output than leetcode
# here the optimal solution


def rearr(nums):
    new=[0]*len(nums) #//array containing zeros only
    size=len(nums)
    N=1
    P=0
    for i in nums:
        if i>=0:
            new[P]=i
            P+=2
        else:
            new[N]=i
            N+=2
    print(new)

nums=[5,10,-3,-1,-10,6]
rearr(nums)

# time and space compexity is O(n)