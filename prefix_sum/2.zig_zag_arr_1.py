# time complexity is O(n(r-l+1)^2) and space complexity is O(r*n-l)
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD=10**9 + 7

        # m 
        r=r-l+1
        dp=[[0] *(r) for _ in range(n)]

        for j in range(r):
            dp[0][j]=1
        
        for i in range(1,n):
            for j in range(r):
                if i%2==0:
                    if j==0:
                        continue
                    else:
                        for k in range(0,j):
                            dp[i][j]=(dp[i][j]+dp[i-1][k])%MOD
                else:
                    if j==r:
                        continue
                    else:
                        for k in range(j+1,r):
                            dp[i][j]=(dp[i][j]+dp[i-1][k])%MOD
        
        return (sum(dp[n-1])*2)%MOD

# Time complexity and space complexity  is O(n*m) 
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD=10**9 + 7

        # m 
        r=r-l+1
        dp=[[0] *(r) for _ in range(n)]

        for j in range(r):
            dp[0][j]=1
        
        for i in range(1,n):
            prev=0

            if i%2==0:
                for j in range(r):
                    dp[i][j]=prev
                    prev = (dp[i][j] + dp[i-1][j]) % MOD
            else:
                for j in range(r-1,-1,-1):
                    dp[i][j]=prev
                    prev=(dp[i][j]+dp[i-1][j]) %  MOD

        return (sum(dp[n-1])*2)%MOD




        



        


        