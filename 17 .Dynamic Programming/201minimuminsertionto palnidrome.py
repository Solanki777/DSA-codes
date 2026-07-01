# here we just have to minius the longest common palindrome to the length of the string 
# time complexity is o(n^2) and space complexity is O(n)
class Solution:
    def minInsertions(self, s: str) -> int:
        rev=s[::-1]

        dp=[0 for _ in range(len(s)+1)] 

        for i in range(1,len(s)+1):
            prev_diag=0

            for j in range(1,len(s)+1):
                temp=dp[j]
                                
                if s[i-1]==rev[j-1]:
                    dp[j]=prev_diag+1
                else:
                    dp[j]=max(dp[j],dp[j-1])
                prev_diag=temp
                
        return len(s)-dp[len(s)]
        