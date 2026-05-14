class Solution:
    
    def minCost(self, height):
        
        def recursion(index):
            if index==0:
                return 0
            
            jm1=recursion(index-1)+abs(height[index]-height[index-1])

            if index>1:
                jm2=recursion(index-2)+abs(height[index]-height[index-2])
            else:
                jm2=float('inf')
            
            return min(jm2,jm1)
        return recursion(len(height)-1)

# TIme complexity is O(2^n)
# space complexity is O(n)

# recursion with dp 
class Solution:
    
    def minCost(self, height):
        dp=[-1]*len(height)
        dp[0]=0
        
        def recursion(index):
            if index==0:
                return 0
            if dp[index]!=-1:
                return dp[index]
            
            jm1=recursion(index-1)+abs(height[index]-height[index-1])

            if index>1:
                jm2=recursion(index-2)+abs(height[index]-height[index-2])
            else:
                jm2=float('inf')
            
            dp[index]=min(jm2,jm1)
            return dp[index]
        
        return recursion(len(height)-1)


# TIme complexity is O(2n)
# space complexity is O(n)

# only dp
class Solution:
    def minCost(self, height):
        dp=[-1]*len(height)
        dp[0]=0

        for index in range(1,len(height)):
            j1=dp[index-1]+abs(height[index-1]-height[index])

            if index>1:
                j2=dp[index-2]+abs(height[index-2]-height[index])
            
            else:
                j2=float('inf')
            
            dp[index]=min(j2,j1)

        return dp[len(height)-1]


# TIme complexity is O(n)
# space complexity is O(n)