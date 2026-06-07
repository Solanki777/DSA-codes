class Solution:
    def recursion(self,s,index,curr,ans):
        if index==-1:
            ans.append(curr)
            return
        
        self.recursion(self,s,index+1,curr+s[index],ans)
        self.recursion(self,s,index+1,curr,ans)

    def lcsprint(self,s1,s2):
        s1=self.recursion(s1,len(s1)-1,"",[])
