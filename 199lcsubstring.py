
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

        



        