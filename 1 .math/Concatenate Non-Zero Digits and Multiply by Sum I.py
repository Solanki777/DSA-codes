# time complexity is O(n) and space complexity is O(1)
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        s=0
        ans=""

        for ch in str(n):
            if int(ch)!=0:
                s+=int(ch)
                ans+=ch
        
        return int(ans)*s
    
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

        


        