
# time and space complexity is O(n^3) 
class Solution:
    def getall(self,s):
        n=len(s)
        ans=set()
        for i in range(n):
            for j in range(i+1,n+1):
                ans.add(s[i:j])
        return ans

    def longCommSubstr(self, s1, s2):
        s_set1=set()
        s_set1=self.getall(s1)
        s_set2=set()
        s_set2=self.getall(s2)
        maxi=0
        for i in s_set1:
            if i in s_set2:
                maxi=max(maxi,len(i))
        return maxi

# let's use recursion time compelxity is O(3^(m+n)) and space complexity is (m+n)
class Solution:
    
    def longCommSubstr(self, s1, s2):
        def recursion(i,j,count):
            if i==len(s1) or j==len(s2):
                return count
            
            if s1[i]==s2[j]:
                count= recursion(i+1,j+1,count+1)
            return max(count,recursion(i+1,j,0),recursion(i,j+1,0))
        return recursion(0,0,0)

# time and space complexity is O(m*n*k)
class Solution:
    def longCommSubstr(self, s1, s2):
        
        dp={}

        def recursion(i,j,count):
            if i==len(s1) or j==len(s2):
                return count
            
            if (i,j,count) in dp:
                return dp[(i,j,count)]
            
            curr=count
            if s1[i]==s2[j]:
                curr= recursion(i+1,j+1,count+1)

            dp[(i,j,count)]=max(curr,recursion(i+1,j,0),recursion(i,j+1,0))
            return dp[(i,j,count)]
        return recursion(0,0,0)
    
# tabulation think about lc for subsequence for common we just add 1 which is right here also but for not common we take past commons for both above i-1 and side j-1 but here if thy are not common then put 0 no need to longer carried out 

# time and space complexity is O(m+n)
class Solution:
    def longCommSubstr(self, s1, s2):
        dp=[[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
        maxi=0

        for i in range(len(s1)):
            if s1[i]==s2[0]:
                dp[0][i]=1
                maxi=1
        for j in range(len(s2)):
            if s2[j]==s1[0]:
                dp[j][0]=1
                maxi=1

        for i in range(1,len(s2)):
            for j in range(1,len(s1)):
                if s2[i]==s1[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                    maxi=max(maxi,dp[i][j])
                
        return maxi
    
# space optimization 
class Solution:
    def longCommSubstr(self, s1, s2):
        prev=[0 for _ in range(len(s1)+1)]
        maxi=0

        for i in range(1,len(s2)):
            curr=[0 for _ in range(len(s1)+1)]

            for j in range(1,len(s1)):
                if s2[i]==s1[j]:
                    curr[j]=1+prev[j-1]
                    maxi=max(maxi,curr[j])
            prev=curr
                
        return maxi

# space optimization to 
class Solution:
    def longCommSubstr(self, s1, s2):
        dp=[0]*len(s1)
        ans=0

        for i in range(len(s2)):

            for j in range(len(s1)-1,-1,-1):
                if s2[i]==s1[j]:
                    if j==0:
                        dp[j]=1
                    else:
                        dp[j]=dp[j-1]+1
                    ans=max(ans,dp[j])
                else:
                    dp[j]=0     

        return ans


         