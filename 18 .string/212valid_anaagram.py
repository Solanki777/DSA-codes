# time and space complexity is O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        count={}

        for char in s:
            if char not in count:
                count[char]=1
            else:
                count[char]+=1
        
        for char in t:
            if char not in count or count[char]==0:
                return False
            else:
                count[char]-=1
        return True
        
            
        
