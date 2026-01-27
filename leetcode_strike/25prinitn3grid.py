class Solution:
    def dpsolution(self,n,dp,raw,prev1,prev2,prev3):
        
        # if raw reaches to the last position we got the 1 solution
        if raw==n:
            return 1
        
        # we can check that this solution is previously exits or not if it does than use it 
        if dp[raw][prev1][prev2][prev3] !=-1:
            return dp[raw][prev1][prev2][prev3]
        
        ans=0
        for c1 in range(3):
            if c1==prev1:
                continue

            for c2 in range(3):
                if c2==prev2 or c2==c1:
                    continue

                for c3 in range(3):
                    if c3==prev3 or c3==c2:
                        continue

                    ans+=self.dpsolution(n,dp,raw+1,c1,c2,c3)

        dp[raw][prev1][prev2][prev3]=ans
        return ans




    def get_ans(self,n):

        # like in first raw and in first column we have to select a color from 3 . So we have to make such dp that can store all the values . Here it size is must be four dimension like 1 dimension is for first choice you make similar we have to make 4 choice 1 extra is for row selection so this is it
        dp=[[[[-1  for _ in range(4)] for _ in range(4)]for _ in range(4)] for _ in range(n)]
        ans=self.dpsolution(n,dp,0,3,3,3)
        return ans
    
print(Solution().get_ans(3))