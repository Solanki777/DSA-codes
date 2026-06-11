# time complexity is O(m*n) and space complexity is O(n)
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




        