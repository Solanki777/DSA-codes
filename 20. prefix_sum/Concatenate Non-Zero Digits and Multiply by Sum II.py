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
    
# just used prefix sum on summation of digits constraints remains same as above
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sum=[0] * len(s)
        su=0
        MOD=10 ** 9 +7
        ans=[]

        for ch in range(len(s)):
            digit=int(s[ch])
            if digit !=0:
                su+=digit
            prefix_sum[ch]=su % MOD

        
        for i,j in queries:

            if i==0:
                x=prefix_sum[j]
            else:
                x=prefix_sum[j]-prefix_sum[i-1]

            temp=""
            for c in range(i,j+1):
                if s[c]!='0':
                    temp+=s[c]



            if temp:
                ans.append(int(temp) * x % MOD )
            else:
                ans.append(0)
        
        return ans

        
# time and space complexity is O(n)
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD=10**9 +7

        n=len(s)

        ps=[0]*n  #for sum
        pc=[0]*n  # for string
        pw=[0]*n  # for power
        
        d=int(s[0])
        ps[0] =d
        pc[0]= d if d!=0 else 0
        pw[0]= 1 if d!=0 else 0

        for i in range(1,n):
            d=int(s[i])
            ps[i]=(ps[i-1]+d) %MOD
            pw[i]=(pw[i-1]+1 )if d!=0 else pw[i-1]
            pc[i]=(pc[i-1]*10 +d)% MOD if d!=0 else pc[i-1]
        
        res=[]
        for l,r in queries:
            sm=(ps[r]-(ps[l-1] if l>0 else 0)) % MOD

            high=pc[r]
            low=pc[l-1] if l-1>=0 else 0

            power=pw[r]-(pw[l-1] if l-1 >=0 else 0)

            ans=(high - low * pow(10 , power , MOD )) % MOD

            sm=(sm*ans) %  MOD

            res.append(sm)

        return res

        



        