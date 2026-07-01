# here they give ciclular array 

# Time complexity is O(2^n) and space complexity is O(2n)
class Solution:
    def recur(self,index,arr):
        
        if index==len(arr)-1:
            return arr[index]
        if index>=len(arr):
            return 0
        pick=self.recur(index+2,arr)+arr[index]
        not_pick=self.recur(index+1,arr)
        return max(pick,not_pick)

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        ans2=self.recur(0,nums[:n-1])
        ans1=self.recur(0,nums[1:n])
        
        return max(ans1,ans2)

# usign dp time complexity is O(n) and space complexity is O(2n)
class Solution:
    def recur(self,index,arr,dp):
        if index==len(arr)-1:
            return arr[index]
        if index>=len(arr):
            return 0
        if dp[index]!=-1:
            return dp[index]
        pick=self.recur(index+2,arr,dp)+arr[index]
        not_pick=self.recur(index+1,arr,dp)
        dp[index]=max(pick,not_pick)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[-1]*(len(nums)-1)
        ans2=self.recur(0,nums[:n-1],dp)
        dp=[-1]*(len(nums)-1)
        ans1=self.recur(0,nums[1:n],dp)
        
        return max(ans1,ans2)
    
# removing recursion time and space complexity is O(n)
class Solution:
    def solve(self,arr):
        n=len(arr)
        if n==1:
            return arr[0]
        dp=[-1]*len(arr)
        
        dp[0]=arr[0]
        dp[1]=max(arr[0],arr[1])

        for i in range(2,n):
            pick=arr[i]+dp[i-2]
            notpick=dp[i-1]
            dp[i]=max(pick,notpick)
        return dp[n-1]
   
        

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        
        
        return max(self.solve(nums[1:]),self.solve(nums[:-1]))
        
# without dp using two pointers time complexity is O(n) and space complexity is O(1)
class Solution:
    def solve(self,arr):
        n=len(arr)
        if n==1:
            return arr[0]
        prev1=arr[0]
        prev2=max(arr[0],arr[1])
        for i in range(2,n):
            pick=arr[i]+prev1
            notpick=prev2
            curr=max(pick,notpick)
            prev1=prev2
            prev2=curr
        return prev2

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        
        return max(self.solve(nums[1:]),self.solve(nums[:-1]))
        
