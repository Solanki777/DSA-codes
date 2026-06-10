# time complexity will be O(n*2^n) and space complexity is O(n) for stack space and O(n^2) where we build each time a new string and store it into the curr so we make 1+2+3+4..+n strings .
class Solution:
    def check_palin(self,curr):
        if curr==curr[::-1]:
            return len(curr)
        return 0
    def recursion(self,index,curr,s,maxi):
        if index==len(s):
            return max(maxi,self.check_palin(curr))
        
        pick=self.recursion(index+1,curr+s[index],s,maxi)
        notPick=self.recursion(index+1,curr,s,maxi)
        return max(pick,notPick)

            
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.recursion(0,"",s,1)
    
# use dp time and space complexity is O(n*2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev=s[::-1]

        dp=[[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        

        for i in range(1,len(s)+1):
            for j in range(1,len(s)+1):
                if s[i-1]==rev[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                
        return dp[len(s)][len(s)]
        