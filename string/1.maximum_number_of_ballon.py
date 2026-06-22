class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        goal={}
        for ch in "balloon":
            if ch not in goal:
                goal[ch]=1
            else:
                goal[ch]+=1
        
        ans={}
        for ch in text:
            if ch in goal:
                
                if ch not in ans :
                    ans[ch]=1
                else:
                    ans[ch]+=1

        mini=float('inf')
        for ch in goal:
            if ch not in ans:
                return 0
            mini=min(mini,ans[ch]//goal[ch])
        return mini

# time complexity is O(n) and space complexity is O(1)
            
        
        
            



        
        



        