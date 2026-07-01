# recursion along with dp 
class Solution:
    def solve(self,nums,index,dp):
        
        
        if index>=len(nums)-1:
            return 0
        if dp[index]!=-1:
            return dp[index]

        if nums[index]==0:
            return float('inf')
        
        mini_jump=float('inf')

        for i in range(1,nums[index]+1):
            jump=self.solve(nums,index+i,dp)
            mini_jump=min(mini_jump,jump+1)
        
        dp[index]=mini_jump

        return dp[index]
    def jump(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        return self.solve(nums,0,dp)
        
# optimal 
# optimal 
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        
        l=0
        r=0
        jump=0

        

        while r<len(nums)-1:
            max_jump=0

            for i in range(l,r+1):
                max_jump=max(max_jump,nums[i]+i)

            if max_jump==r:
                return float('inf')
                
            l=r+1
            r=max_jump
                
            jump+=1
        return jump
    
# time complexity is O(n) and spacec complexity is o(1)



        