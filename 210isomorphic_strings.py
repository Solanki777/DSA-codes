# time complexity is O(n) and space complexity is O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seta={}
        setb={}

        for i in range(len(s)):
            if s[i] in seta and seta[s[i]]!=t[i]:
                return False
            
            if t[i] in setb and setb[t[i]]!=s[i]:
                return False
            
            seta[s[i]]=t[i]
            setb[t[i]]=s[i]
            
        return True