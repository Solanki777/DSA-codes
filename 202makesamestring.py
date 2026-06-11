# pure recursion time complexity is O(2^m+n) space ocmplexity is O(m+n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def f(i,j):
            if i==len(word1):
                return len(word2)-j

            if j==len(word2):
                return len(word1)-i

            if word1[i]==word2[j]:
                return f(i+1,j+1)

            return 1+min(
                f(i+1,j),
                f(i,j+1)
            )

        return f(0,0)

# dp inserted 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1 for _ in range(len(word2))] for _ in range(len(word1))]

        def f(i,j):
            if i==len(word1):
                return len(word2)-j

            if j==len(word2):
                return len(word1)-i
            
            if dp[i][j]!=-1:
                return dp[i][j]

            if word1[i]==word2[j]:
                return f(i+1,j+1)

            dp[i][j]= 1+min(
                f(i+1,j),
                f(i,j+1)
            )
            return dp[i][j]

        return f(0,0)
    
# tabulation 


# time complexity is O(m*n) and space complexity is O(n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp=[[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):

                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1

                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])

        
        lcs=dp[len(word1)][len(word2)]
        deletion=len(word2)-lcs
        ans=deletion+(len(word1)-lcs)
        return ans




        
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # first we find the lcs between two strings 
        dp=[0 for _ in range(len(word2)+1)]

        for i in range(1,len(word1)+1):
            prev_diag=0

            for j in range(1,len(word2)+1):
                temp=dp[j]

                if word1[i-1]==word2[j-1]:
                    dp[j]=prev_diag+1

                else:
                    dp[j]=max(dp[j],dp[j-1])

                prev_diag=temp
        
        lcs=dp[len(word2)]
        deletion=len(word2)-lcs
        ans=deletion+(len(word1)-lcs)
        return ans




        