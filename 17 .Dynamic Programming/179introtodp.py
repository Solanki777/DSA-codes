# # Q - Find the Fiboncci seriese

# 1. Recursion[ Top Down uproach]:
# Time compexity is O(2N) and Space complexity is stack space O(N)
class solution:
    def feb(self,val):
        if val==0:
            return 0
        if val==1:
            return 1
        return self.feb(val-2) +self.feb(val-1)

# 2. Memorization[Top down uproach]:
# Time complexity is O(N) and Space complexity O(N) for stack space + Dp array O(n)


class Solution:
    def solve(self,st,end,dp):
        if st>end:
            return dp[end]
        dp[st]=dp[st-1]+dp[st-2]
        st+=1
        return self.solve(st,end,dp)
        

    def fib(self, n: int) -> int:
        
        
        if n==0:
            return 0
        if n==1:
            return 1
        dp=[0]*(n+1)
        dp[1]=1
        
        return self.solve(2,n,dp)
    
# 3. Tabulation:
# Time commplexity is O(n) and space complexity is O(N) for Dp arry
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

# 4. Tabulation with space optimization:
# Time complexity is O(n) and space complexity is O(1)
class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        prev2 = 0
        prev1 = 1

        for i in range(2, n + 1):

            curr = prev1 + prev2

            prev2 = prev1
            prev1 = curr

        return prev1