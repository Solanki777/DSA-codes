# time complexity is O(m^2) where m is non-zero elements and space complexity is O(ans)
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        ans=[]
        MOD=10 ** 9 + 7

        for i, j in queries:
            su=0
            x=0
            temp=""
            for k in range(i,j+1):
                if int(s[k])!=0:
                    su+=int(s[k])
                    temp+=s[k]
            
            if temp :
                ans.append(int(temp)*su %MOD)
            else:
                ans.append(0)
        
        return ans

        