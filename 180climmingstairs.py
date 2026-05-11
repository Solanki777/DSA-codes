# using recursion : Time comlexity is O(2^n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

# using recursion + dp  time ocmplexity is O(n) and space complexity is stack space O(n) + dp O(n)
class Solution:
    def solve(self,dp,n):
        if dp[n]!=0:
            return dp[n]
        dp[n]=self.solve(dp,n-1)+self.solve(dp,n-2)
        return dp[n]
        
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        return self.solve(dp,n)
        
# Only dp no recursion : time and space complexity is O(n) No recursion stack space
class Solution:
    def climbStairs(self, n: int) -> int:
            if n==1:
                return 1
            if n==2:
                return 2
            dp=[0]*(n+1)
            dp[1]=1
            dp[2]=2
            for i in range(3,n+1):
                dp[i]=dp[i-1]+dp[i-2]
            return dp[n]
