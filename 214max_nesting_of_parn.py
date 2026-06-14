# time complexity is O(n) and space compexity is O(1)

class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        maxi=0
        for i in s:
            if i=="(":
                depth+=1
                maxi=max(maxi,depth)
            elif i==")":
                depth-=1
        return maxi 
        