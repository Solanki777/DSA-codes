# time complexity and space complexity is O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        i = len(s) - 1
        ans=[]
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            
            j=i
            if i<0:
                break
            while i>=0 and s[i]!=" ":
                i-=1
            ans.append(s[i+1:j+1])
        return " ".join(ans)
    
# space optimization
           
