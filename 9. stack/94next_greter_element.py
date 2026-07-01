# bruteforce solution 

# class Solution:
#     def nextLargerElement(self, arr):
#         # base value 
#         if len(arr)==1:
#             return [-1]

#         ans=[-1]*(len(arr))

        
#         for i in range(len(arr)-1):
#             curr=arr[i]
            
#             for j in range(i+1,len(arr)):
#                 if curr<arr[j]:
#                     ans[i]=arr[j]
#                     break
#         ans[i+1]=-1
        
#         return ans
# time complexity is O(N^2) and space complexity is O(N)
# sl=Solution()
# arr=[6,8,0,1,3]
# sl.nextLargerElement(arr)

# optimal solution : here we use the monotonic stack. The monotonic stack is type of stack which follows the characteristics followd by the codder . here we give characteristics that the stack only store data in ascending order from top to bottom

class Solution:
    def nextLargerElement(self, arr):
        ans=[-1]*(len(arr)-1)
        stack=[]

        for i in range(len(arr)-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            stack.append(arr[i])

        
        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)

sl=Solution()
arr=[6,8,0,1,3]
sl.nextLargerElement(arr)

        