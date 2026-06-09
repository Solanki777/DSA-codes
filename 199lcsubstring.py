
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


        