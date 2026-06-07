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
                
