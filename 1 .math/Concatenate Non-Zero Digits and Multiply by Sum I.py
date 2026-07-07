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


        