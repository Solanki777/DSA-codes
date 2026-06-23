# time complexity is O((r-l)^n) and space complexity is O(n)
class Solution:
    def recursion(self,prev2,prev1,index,n,l,r):
        if index==n:
            return 1

        ans=0

        for i in range(l,r+1):
            if prev1!=-1 and i==prev1:
                continue

            if prev2!=-1 and prev1!=-1:
                
                if prev2<prev1<i:
                    continue
                if prev2>prev1>i:
                    continue

            ans+=self.recursion(prev1,i,index+1,n,l,r)

        return ans

    def zigZagArrays(self,n:int,l:int,r:int)->int:
        return self.recursion(-1,-1,0,n,l,r)

# dp + recursion solution time complexity is O(nm^2)*m recurisons stack and space complexity is O(nm^2)
class Solution:
    def recursion(self,prev2,prev1,index,n,l,r,dp):
        if index==n:
            return 1

        key=(prev2,prev1,index)
        
        if key in dp:
            return dp[key]

        ans=0

        for i in range(l,r+1):
            if prev1!=-1 and i==prev1:
                continue

            if prev2!=-1 and prev1!=-1:
                
                if prev2<prev1<i:
                    continue
                if prev2>prev1>i:
                    continue

            ans+=self.recursion(prev1,i,index+1,n,l,r,dp)
        dp[key]=ans % (10**9 + 7)

        return dp[key]

    def zigZagArrays(self,n:int,l:int,r:int)->int:
        dp={}
        return self.recursion(-1,-1,0,n,l,r,dp)


# time and space complexity is O(nm)
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD=10**9 + 7
        r-=l
        dp=[[0] *(r+1) for _ in range(n)]

        for j in range(r+1):
            dp[0][j]=1
        
        for i in range(1,n):
            prev=0
            if i%2==1:
                for j in range(r+1):
                    dp[i][j]=prev
                    prev=(prev+dp[i-1][j])%MOD
            else:
                for j in range(r,-1,-1):
                    dp[i][j]=prev
                    prev=(prev+dp[i-1][j])%MOD
        
        return sum(dp[-1]*2)%MOD



        