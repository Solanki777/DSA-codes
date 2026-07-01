# # bruteforce soltuion:
# def lsc(nums):
#     max_c=0
#     for i in range(len(nums)):
#         msx=1
#         num=nums[i]
#         while num+1 in nums:
#             msx+=1
#             num=num+1
#         max_c=max(msx,max_c)
#     return max_c


# nums=[1,99,101,98,2,5,3,100,1,1]
# ans=lsc(nums)
# print(ans)
# time complexity is O(N^2) and space coplexity is O(N)

# other method is apply first sorting then find the longest common subsequent
# def lsc(nums):
#     nums.sort()
#     last_small=float("-inf")
#     count=0
#     max_c=0
#     print(nums)
#     for i in range(len(nums)):
#         if last_small==nums[i]-1:
#             count+=1
#             last_small=nums[i]
#         else:
#             count=1
#             last_small=nums[i]
#         max_c=max(max_c,count)
#     return max_c



# nums=[1,99,101,98,2,5,3,100,1,1]
# ans=lsc(nums)
# print(ans)


# here suppose time coplexity for sorting an arry is nlogn and for tranversing aay single time so overall time compelxity is O(N+NlogN) and space copelxity is O(1)


# optimal solution

def lsc(nums):
    my_set=set(nums)
    long=0
    
    for el in my_set:
        if el-1 not in my_set:
            count=1
            num=el
            while num+1 in my_set:
                count+=1
                num+=1
        long=max(long,count)
    return long

nums=[1,99,101,98,2,5,3,100,1,102]
ans=lsc(nums)
print(ans)

# time coplexity is O(3n) here n for traversing set to convert arry into set,other n is to traversing set and last n is after finding the first number it has to go for find the next element . And space complexity is O(n)