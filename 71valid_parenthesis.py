class Solution:
    def brac(self,ind,total,n,braces,ans):
        
        # if first is put ")" then it is invalid so it give -1 as sum and also if ((( for n = 2 then there we can not put 3 closing braces so if total(3)>n then it is also invalid
        if total<0 or total>n:
            return

        # first check we reach at last     
        if len(braces)==ind:
            # if it is zero than we found the right ans 
            if total==0:
                ans.append("".join(braces))
            
            # else we only reach last without getting right ans 
            return
        
        braces[ind]="("
        self.brac(ind+1,total+1,n,braces,ans)
        braces[ind]=")"
        self.brac(ind+1,total-1,n,braces,ans)
        
n=2
s=Solution()
braces=[""]*(n*2)
ans=[]
s.brac(0,0,n,braces,ans)
print(ans)