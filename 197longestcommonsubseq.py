# extream bruteforces solution 
# time and space complexity is O(m*2^m + n*2^n)
class Solution:
    def subseqgenerator(self,s,index,curr,result):
        if index==len(s):
            result.append(curr)
            return

        self.subseqgenerator(s,index+1,curr+s[index],result)
        self.subseqgenerator(s,index+1,curr,result)
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sub1=[]
        sub2=[]
        self.subseqgenerator(text1,0,"",sub1)
        self,self.subseqgenerator(text2,0,"",sub2)

        set2=set(sub2)
        ans=0

        for sub in sub1:
            if sub in set2:
                ans=max(ans,len(sub))
        return ans
    
# recursion and compare at the same time : time complexity is O(2^(m+n)) and space complexity is O(max(len(m) , len(n)))
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recursion(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            if text1[ind1]==text2[ind2]:
                return 1+recursion(ind1-1,ind2-1)
            return max(recursion(ind1-1,ind2),recursion(ind1,ind2-1))
        return recursion(len(text1)-1,len(text2)-1)

# time and space complexity is O(m*n) in addition of space complexity of O(m+n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def recursion(ind1,ind2):
            if ind1<0 or ind2<0:
                return 0
            
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            
            if text1[ind1]==text2[ind2]:
                dp[ind1][ind2]= 1+recursion(ind1-1,ind2-1)
            else:
                dp[ind1][ind2]= max(recursion(ind1-1,ind2),recursion(ind1,ind2-1))
            return dp[ind1][ind2]
        return recursion(len(text1)-1,len(text2)-1)

