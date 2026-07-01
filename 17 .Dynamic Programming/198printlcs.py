# extream brute force solution with time and space complexity of O(m*2^m + n*2^n)
class Solution:
    def recursion(self,s,index,curr,ans):
        if index==-1:
            ans.append(curr)
            return
        
        self.recursion(s,index-1,curr+s[index],ans)
        self.recursion(s,index-1,curr,ans)

    def lcsprint(self,s1,s2):
        ans1=[]
        ans2=[]

        self.recursion(s1,len(s1)-1,"",ans1)
        self.recursion(s2,len(s2)-1,"",ans2)

        s2=set(ans2)
        ans=""
        for s in ans1:
            if s in s2:
                if len(s)>len(ans):
                    ans=s
        return ans

# time and space complexity is O(m*n)
class Solution:
    def lcsprint(self,s1,s2):

        # first build the dp 
        dp=[[0 for _ in range(len(s1))] for _ in range(len(s2))]

        for i in range(len(s1)):
            if s1[i]==s2[0]:
                dp[0][i]=1

            elif i>0 :
                dp[0][i]=dp[0][i-1]

        for i in range(len(s2)):
            if s2[i]==s1[0]:
                dp[i][0]=1

            elif i>0 :
                dp[i][0]=dp[i-1][0]
        
        for i in range(1,len(s2)):
            for j in range(1,len(s1)):
                if s1[j]==s2[i]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        # Now backtracking
        i=len(s2)-1
        j=len(s1)-1
        ans=[]

        while i >=0 and j>=0:
            if s1[j]==s2[i]:
                ans.append(s1[j])
                i=i-1
                j=j-1
            else:
                if i>0 and dp[i-1][j]>=dp[i][j-1]:
                    i-=1
                elif j>0:
                    j-=1
                else:
                    break

        return ''.join(reversed(ans))
