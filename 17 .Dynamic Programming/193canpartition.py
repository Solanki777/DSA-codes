# time complexity is O(2*n) and space complexity O(n)
class Solution:
    def recursion(self,nums,index,curr,s):
        if curr==s:
            return True
        if curr>s or index>=len(nums):
            return False
        
        inlcude=self.recursion(nums,index+1,curr+nums[index],s)
        
        not_inlcude=self.recursion(nums,index+1,curr,s)

        return inlcude or not_inlcude

    def canPartition(self,nums):
        s=sum(nums)
        if s%2!=0:
            return False
        s=s/2
        return self.recursion(nums,0,0,s)

# time complexity is O(n*s//2) and space compelxity is O(n)+O(s//2*n)
class Solution:
    def recursion(self,nums,index,curr,s,dp):
        if dp[index][curr]!=-1:
            return dp[index][curr]
        
        if curr==s:
            return True
        if curr>s or index>=len(nums):
            return False
        
        inlcude=self.recursion(nums,index+1,curr+nums[index],s)
        
        not_inlcude=self.recursion(nums,index+1,curr,s)

        dp[index][curr]= inlcude or not_inlcude
        return dp[index][curr]
        

    def canPartition(self,nums):
        s=sum(nums)
        if s%2!=0:
            return False
        s=s//2
        dp=[[-1 for _ in range(s)] for _ in range(len(nums))]
        return self.recursion(nums,0,0,s,dp)

# tabulation Time and space comlexity is O(len(nums)*s)
class Solution:
    def canPartition(self,nums):
        s=sum(nums)
        if s%2!=0:
            return False
        s=s//2
        dp=[[False for _ in range(s+1)] for _ in range(len(nums))]
        
        for i in range(len(nums)):
            dp[i][0]=True

        if nums[0]<=s:
            dp[0][nums[0]]=True
        
        for i in range(1,len(nums)):
            for j in range(1,s+1):
                include=False
                not_include=dp[i-1][j]

                if j>=nums[i]:
                    include=dp[i-1][j-nums[i]]
                
                dp[i][j]=include or not_include
        return dp[len(nums)-1][s]
    
# improve space complexity to O(s)
class Solution:
    def canPartition(self,nums):
        s=sum(nums)
        if s%2!=0:
            return False
        s=s//2
        prev=[False for _ in range(s+1)]
        
        prev[0]=True

        if nums[0]<=s:
            prev[nums[0]]=True
        
        for i in range(1,len(nums)):
            curr=[False for _ in range(s+1)]
            curr[0]=True

            for j in range(1,s+1):
                include=False
                not_include=prev[j]

                if j>=nums[i]:
                    include=prev[j-nums[i]]
                
                curr[j]=include or not_include
            prev=curr
        return prev[s]



