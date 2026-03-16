# # brute force solution 
# class Solution:
#     def nextGreaterElements(self, nums) :
#         size=len(nums)
#         ans=[-1]*len(nums)
#         for i in range(0,size):
#             curr=nums[i]

#             for j in range(1,size):
#                 next_index=(i+j)%size
#                 if curr<nums[next_index]:
#                     ans[i]=nums[next_index]
#                     break

#         print(ans)

# # time complexity is O(N^2) and space complexity is O(n)

# sl=Solution()
# nums=[2,10,12,1,11]
# sl.nextGreaterElements(nums)

# optimal using two stack

class Solution:
    def nextGreaterElements(self, nums) :
        size=len(nums)
        ans=[-1]*size
        stack=[]

        # stack filling
        for i in range(size-1,-1,-1):
            while stack and stack[-1]<nums[i]:
                    stack.pop()
                    
            stack.append(nums[i])
        print(stack)

        # now using the stack 
        for i in range(size-1,-1,-1):
            while stack and stack[-1]<= nums[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(nums[i])
        print(ans)
            
                


sl=Solution()
nums=[2,10,12,1,11]
sl.nextGreaterElements(nums)

# Time complexity is O(n) and space complexity is O(n)
        